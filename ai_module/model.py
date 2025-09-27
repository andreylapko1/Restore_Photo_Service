import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim



CLEAN_IMG = r"C:\Users\andre\PycharmProjects\Restore_Photo_Service\ai_module\lerning\bee-on-daisy.jpg"
NOISY_IMG = r"C:\Users\andre\PycharmProjects\Restore_Photo_Service\ai_module\lerning\bee-on-daisy_bad.jpg"

clean = cv2.imread(CLEAN_IMG)
noisy = cv2.imread(NOISY_IMG)

clean = cv2.cvtColor(clean, cv2.COLOR_BGR2RGB)
noisy = cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB)

clean = cv2.resize(clean, (256, 256)).astype(np.float32) / 255.00
noisy = cv2.resize(noisy, (256, 256)).astype(np.float32) / 255.00


clean = torch.from_numpy(clean).permute(2,0,1).unsqueeze(0)
noisy = torch.from_numpy(noisy).permute(2,0,1).unsqueeze(0)


class SimpleRestorer(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 3, 3, padding=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.layers(x)


model = SimpleRestorer()
crit = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


for epoch in range(100):
    optimizer.zero_grad()
    output = model(noisy)
    loss = crit(output, clean)
    loss.backward()
    optimizer.step()
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

out = output.detach().squeeze(0).permute(1,2,0).numpy()
out = (out * 255).clip(0,255).astype(np.uint8)
out_bgr = cv2.cvtColor(out, cv2.COLOR_RGB2BGR)
cv2.imwrite("restored.png", out_bgr)
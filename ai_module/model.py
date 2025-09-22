import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim



CLEAN_IMG = r"C:\Users\andre\PycharmProjects\Restore_Photo_Service\ai_module\lerning\bee-on-daisy.jpg"
img = cv2.imread(CLEAN_IMG)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (64, 64))
img = img.astype(np.float32)
clean = torch.from_numpy(img).permute(2,0,1).unsqueeze(0)

noisy = clean + 0.1 * torch.randn_like(clean)
noisy = noisy.clamp(0,1)

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

out = output.detach().squeeze(0).permute(1,2,0).numpy()
out = (out * 255).clip(0,255).astype(np.uint8)
out_bgr = cv2.cvtColor(out, cv2.COLOR_RGB2BGR)
cv2.imwrite("restored2.png", out_bgr)


torch.save(model.state_dict(), "restorer.pth")

model.load_state_dict(torch.load("restorer.pth"))
model.eval()
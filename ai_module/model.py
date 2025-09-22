import torch.nn as nn
import torch.optim as optim

class SimpleRestorer(nn.Module):
    def __init__(self):
        super().__init__()
        layers = nn.Sequential(
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
import torch
from torch import nn


class FFNN(nn.Module):
    def __init__(self, n_nodes, n_links):
        super(FFNN, self).__init__()
        n = n_nodes * n_nodes + n_links * 2 + n_links * n_nodes
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(n, 2 * n + 1), nn.ReLU(), nn.Linear(2 * n + 1, n_links)
        )

    def forward(self, x):
        x = torch.cat((tensor.flatten() for tensor in x))
        logits = self.linear_relu_stack(x)
        return logits


device = "cuda" if torch.cuda.is_available() else "cpu"

model = FFNN(104, 103).to(device)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

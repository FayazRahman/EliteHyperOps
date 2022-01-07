import pickle
import torch
from torch import nn
from torch.utils.data import Dataset


class FrankWolfeDataset(Dataset):
    def __init__(self, file):
        self.file = file
        with open(self.file, "rb") as f:
            self.data = pickle.load(f)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        x, y = self.data[idx]

        return x, y


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(113, 2 * 113 + 1), nn.ReLU(), nn.Linear(113 * 2 + 1, 50)
        )

    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits

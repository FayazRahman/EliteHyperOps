import torch
import numpy as np
import data as dt
from model import TrafficFlowModel
from nn_model import NeuralNetwork

demand = [
    1000,
    1500,
    1250,
    1300,
    1000,
    450,
    1200,
    1300,
    1030,
    1000,
    600,
    1050,
    1200,
]  # custom demands

mod = TrafficFlowModel(
    dt.graph, dt.origins, dt.destinations, demand, dt.free_time, dt.capacity
)

link_info_matrix = np.concatenate(
    [mod._link_capacity[:, np.newaxis], mod._link_free_time[:, np.newaxis]],
    axis=1,
)


def turn_off_braess(idx):
    link_idx = dt.braess_idxs[idx]
    mod._link_capacity[link_idx] = 1
    mod._link_free_time[link_idx] = 1000


def turn_on_braess(idx):
    link_idx = dt.braess_idxs[idx]
    mod._link_capacity[link_idx] = dt.capacity[link_idx]
    mod._link_free_time[link_idx] = dt.free_time[link_idx]


def get_input(demand):
    x = torch.tensor(
        np.concatenate(
            [
                link_info_matrix.flatten(),
                demand,
            ]
        )
    )

    return x

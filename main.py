from itertools import combinations
import torch
import numpy as np
import data as dt
from model import TrafficFlowModel
from nn_model import NeuralNetwork
device = "cuda" if torch.cuda.is_available() else "cpu"
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
]  # sample demands

model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("frank_wolfe_nn", map_location=torch.device(device)))
model.eval()

mod = TrafficFlowModel(
    dt.graph, dt.origins, dt.destinations, demand, dt.free_time, dt.capacity
)# initialize traffic model

def run(demand):
    """Run Frank Wolfe NN and return average time of paths in use."""
    x = torch.tensor(
        np.concatenate(
            [
                get_link_info(),
                demand,
            ]
        )
    )

    with torch.no_grad():
        y = model(x.float()).numpy()

    y = y * (y > 0)

    LP_matrix = mod._network.LP_matrix()
    z = (y > 100)[  # only conisdering links with more than 100 flow
        np.newaxis, :
    ].transpose() * LP_matrix
    paths_in_use = [
        i for i in range(LP_matrix.shape[1]) if (z[:, i] == LP_matrix[:, i]).all()
    ]

    link_times = mod.link_flow_to_link_time(y)
    path_times = mod.link_time_to_path_time(link_times)

    avg_time = np.sum(path_times[paths_in_use]) / len(paths_in_use)

    return avg_time





def get_link_info(): #changed the name of get_link_info_matrix to get_link_info
    link_info_matrix = np.concatenate(
        [mod._link_capacity[:, np.newaxis], mod._link_free_time[:, np.newaxis]],
        axis=1,
    )
    return link_info_matrix


def turn_off_braess(idx):
    link_idx = idx #dt.braess_idxs[idx]
    mod._link_capacity[link_idx] = 1
    mod._link_free_time[link_idx] = 1000


def turn_on_braess(idx):
    link_idx = idx
    mod._link_capacity[link_idx] = dt.capacity[link_idx]
    mod._link_free_time[link_idx] = dt.free_time[link_idx]


def get_input(demand):
    x = torch.tensor(
        np.concatenate(
            [
                get_link_info().flatten(),
                demand,
            ]
        )
    )

    return x


def get_best_state(demand):
    state = list()
    min = 100000000
    for k in range(1,6):
        comb = combinations(dt.braess_idxs,k)
        for j in comb:
            turn_off_braess(c for c in j)
            avg_time = run(demand)

            if avg_time < min:
                min = avg_time
                state = (j)
            turn_on_braess(c for c in j)
    return state

print(get_best_state(demand))


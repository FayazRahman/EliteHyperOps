from os import link
import numpy as np
from model import TrafficFlowModel
import data as dt
import pickle

FILENAME = "train_dataset"


def create_dataset(num_data_points, low, high):
    with open(FILENAME, "ab") as f:
        for i in range(num_data_points):
            demand = np.random.randint(low, high, (13,))

            n = np.random.randint(0, 25)
            drop_links = np.random.choice(dt.braess_idxs, n)
            free_time, capacity = dt.free_time.copy(), dt.capacity.copy()

            for drop_idx in drop_links:
                free_time[drop_idx] = 1000
                capacity[drop_idx] = 1

            mod = TrafficFlowModel(
                dt.graph, dt.origins, dt.destinations, demand, free_time, capacity
            )

            link_info_matrix = np.concatenate(
                [mod._link_capacity[:, np.newaxis], mod._link_free_time[:, np.newaxis]],
                axis=1,
            )

            x = np.concatenate(
                [
                    link_info_matrix.flatten(),
                    mod._demand,
                ]
            )

            mod._conv_accuracy = 1e-5
            mod.solve()
            link_flow, link_time, path_time, link_vc = mod._formatted_solution()

            pickle.dump((x, link_flow), f)

            print(i)

    data = []
    with open(FILENAME, "rb") as f:
        for i in range(num_data_points):
            data.append(pickle.load(f))

    with open(FILENAME, "wb") as f:
        pickle.dump(data, f)
create_dataset(50, 100, 1300)

import numpy as np
from model import TrafficFlowModel
import data as dt

# Initialize the model by data
mod = TrafficFlowModel(
    dt.graph, dt.origins, dt.destinations, dt.demand, dt.free_time, dt.capacity
)

# lp_matrix = mod._network.LP_matrix()
# link_info_matrix = np.concatenate(
#     [mod._link_capacity[:, np.newaxis], mod._link_free_time[:, np.newaxis]], axis=1
# )

# demands = mod._demand
# n_nodes = len(dt.graph)
# od_demand_matrix = np.zeros((n_nodes, n_nodes))

# idx = 0
# for i, j in mod._network.OD_pairs():
#     od_demand_matrix[int(i) - 1, int(j) - 1] = demands[idx]
#     idx += 1

# print(lp_matrix)
# print(link_info_matrix)
# print(od_demand_matrix)

# print(lp_matrix.shape)
# print(link_info_matrix.shape)
# print(od_demand_matrix.shape)

# Change the accuracy of solution if necessary
mod._conv_accuracy = 1e-6

# Display all the numerical details of
# each variable during the iteritions
# mod.disp_detail()

# Set the precision of display, which influences
# only the digit of numerical component in arrays
mod.set_disp_precision(4)

# Solve the model by Frank-Wolfe Algorithm
mod.solve()

# Generate report to console
mod.report()

# Return the solution if necessary
link_flow, link_time, path_time, link_vc = mod._formatted_solution()

np.savetxt("linkflowfile", link_flow, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
np.savetxt("linktimefile", link_time, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
np.savetxt("pathtimefile", path_time, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)

#print(path_time)

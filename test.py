from objects import *
from frank_wolfe import findEquilibrium

net = Network()
net.addLink(0, 1, 25, 4)
net.addLink(0, 1, 20, 3)
net.addLink(0, 1, 10, 2)
net.addDemand(0, 1, 10)

eq_flows, eq_times = findEquilibrium(*net.getMatrices(), graph=True)

print(eq_flows)
print(eq_times)

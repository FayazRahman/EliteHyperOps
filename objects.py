import numpy as np


class Link:
    def __init__(self, id, orig, dest, fft, capacity):
        self.id = id
        self.orig = orig
        self.dest = dest
        self.fft = fft
        self.capacity = capacity


class Network:
    def __init__(self):
        self.nodes = set()
        self.links = {}
        self.oddemands = {}
        self.link_num = 0
        self.LinkNodeMatrix = None
        self.LinkInfoMatrix = None
        self.ODDemandMatrix = None

    def addLink(self, orig, dest, fft, capacity):
        self.nodes = set.union(self.nodes, {orig, dest})
        link = Link(self.link_num, orig, dest, fft, capacity)
        self.links[self.link_num] = link
        self.link_num += 1

    def addDemand(self, orig, dest, demand):
        self.oddemands[(orig, dest)] = demand

    def getMatrices(self, random_od=False, min_demand=None, max_demand=None):
        n_links = self.link_num
        n_nodes = len(self.nodes)
        LinkNodeMatrix = np.zeros((n_links, n_nodes))
        LinkInfoMatrix = np.zeros((n_links, 2))

        if random_od:
            ODDemandMatrix = np.random.randint(
                min_demand, max_demand, (n_nodes, n_links)
            )
        else:
            ODDemandMatrix = np.zeros((n_nodes, n_nodes))
            for od, demand in self.oddemands.items():
                ODDemandMatrix[od] = demand

        for i, link in self.links.items():
            LinkNodeMatrix[i, link.orig] -= 1
            LinkNodeMatrix[i, link.dest] += 1

            LinkInfoMatrix[i] = link.fft, link.capacity

        return LinkNodeMatrix, LinkInfoMatrix, ODDemandMatrix

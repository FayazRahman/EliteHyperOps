from objects import Network

ESCALATOR_CAPACITY = 6750  # persons per hour
AVERAGE_WALKING_SPEED = 5000  # metres per hour
P_PB_CAPACITY = 200  # platform to pod bay capacity in persons per hour
P_PB_DST = 26  # platform to first pod bay distance
PB_PB_DST = 13  # distance between consecutive pod bays

network = Network()


def addPlatform(last_node, pod_bays=6):
    curr = last_node + 1

    network.addLink(curr, curr + 1, 1 / 60, ESCALATOR_CAPACITY)  # ticketing to platform
    curr += 1

    for i in range(0, pod_bays):
        network.addLink(
            curr,
            curr + i + 1,
            (P_PB_DST + i * PB_PB_DST) / AVERAGE_WALKING_SPEED,
            P_PB_CAPACITY,
        )  # platform entrance to pod bays

    curr += 6
    return curr

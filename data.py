TICKETING_TO_PLATFORM_CAPACITY = 1300  # persons per hour
AVG_WALKING_SPEED = 5000  # metres per hour
P_P_CAPACITY = 1300  # braess route capacity
P_P_DST = 8  # distance between consecutive platforms


graph = [
    (
        "27",
        ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"],
    ),
    ("14", ["1","27","15"]),
    ("15", ["2","14","16","27"]),
    ("16", ["3","27","15","17"]),
    ("17", ["4","27","16","18"]),
    ("18", ["5","27","17","19"]),
    ("19", ["6","27","18","20"]),
    ("20", ["7","27","19","21"]),
    ("21", ["8","27","20","22"]),
    ("22", ["9","27","21","23"]),
    ("23", ["10","27","24","22"]),
    ("24", ["11","27","23","25"]),
    ("25", ["12","27","24","26"]),
    ("26", ["13","27","25"]),
    ("1", ["2"]),
    ("2", ["3", "1"]),
    ("3", ["4", "2"]),
    ("4", ["5", "3"]),
    ("5", ["6", "4"]),
    ("6", ["7", "5"]),
    ("7", ["8", "6"]),
    ("8", ["9", "7"]),
    ("9", ["10", "8"]),
    ("10", ["11", "9"]),
    ("11", ["12", "10"]),
    ("12", ["13", "11"]),
    ("13", ["12"]),
]

braess_idxs = list(range(26, 49))

capacity = [1000] * 13 + [TICKETING_TO_PLATFORM_CAPACITY] * 13 + [P_P_CAPACITY] * 24
"""    
                ^                         ^                               ^  
        drop off to ticketing     ticketing to platform           platform to platform
               1000                      1300                             1300
"""

free_time = [2 / 60] * 13 + [3 / 60] * 13 + [0.5 / 60] * 24
"""            ^               ^                ^
            2 mins           3 mins          30 secs
"""

# Origin-destination pairs
origins = ["27"]
destinations = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]


# Demand between each OD pair (Conjugated to the Cartesian
# product of Origins and destinations with order)

demand = [
    300,
    300,
    220,
    230,
    100,
    125,
    120,
    130,
    103,
    100,
    220,
    205,
    120,
]  # sample demand

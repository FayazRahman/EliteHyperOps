ESCALATOR_CAPACITY = 6750  # persons per hour
AVG_WALKING_SPEED = 5000  # metres per hour
P_PB_CAPACITY = 2000  # platform to pod bay capacity in persons per hour
P_P_CAPACITY = 2000  # braess route capacity
P_PB_DST = 26  # platform to first pod bay distance
PB_PB_DST = 13  # distance between consecutive pod bays
P_P_DST = 13  # distance between consecutive platforms

graph = [
    (
        "105",
        [
            "92",
            "93",
            "94",
            "95",
            "96",
            "97",
            "98",
            "99",
            "100",
            "101",
            "102",
            "103",
            "104",
        ],
    ),
    ("92", ["1"]),
    ("93", ["2"]),
    ("94", ["3"]),
    ("95", ["4"]),
    ("96", ["5"]),
    ("97", ["6"]),
    ("98", ["7"]),
    ("99", ["8"]),
    ("100", ["9"]),
    ("101", ["10"]),
    ("102", ["11"]),
    ("103", ["12"]),
    ("104", ["13"]),
    ("1", ["2", "14", "15", "16", "17", "18", "19"]),
    ("2", ["1", "3", "20", "21", "22", "23", "24", "25"]),
    ("3", ["2", "4", "26", "27", "28", "29", "30", "31"]),
    ("4", ["3", "5", "32", "33", "34", "35", "36", "37"]),
    ("5", ["4", "6", "38", "39", "40", "41", "42", "43"]),
    ("6", ["5", "7", "44", "45", "46", "47", "48", "49"]),
    ("7", ["6", "8", "50", "51", "52", "53", "54", "55"]),
    ("8", ["7", "9", "56", "57", "58", "59", "60", "61"]),
    ("9", ["8", "10", "62", "63", "64", "65", "66", "67"]),
    ("10", ["9", "11", "68", "69", "70", "71", "72", "73"]),
    ("11", ["10", "12", "74", "75", "76", "77", "78", "79"]),
    ("12", ["11", "13", "80", "81", "82", "83", "84", "85"]),
    ("13", ["12", "86", "87", "88", "89", "90", "91"]),
] + [(str(n), []) for n in range(14, 92)]

capacity = (
    [2000] * 13
    + [ESCALATOR_CAPACITY] * 13
    + [P_P_CAPACITY, *[P_PB_CAPACITY] * 6]
    + [P_P_CAPACITY, P_P_CAPACITY, *[P_PB_CAPACITY] * 6] * 11
    + [P_P_CAPACITY, *[P_PB_CAPACITY] * 6]
)


free_time = (
    [0.5 / 60] * 13
    + [1 / 60] * 13
    + [
        P_P_DST / AVG_WALKING_SPEED,
        *[(P_PB_DST + i * PB_PB_DST) / AVG_WALKING_SPEED for i in range(6)],
    ]
    + [
        P_P_DST / AVG_WALKING_SPEED,
        P_P_DST / AVG_WALKING_SPEED,
        *[(P_PB_DST + i * PB_PB_DST) / AVG_WALKING_SPEED for i in range(6)],
    ]
    * 11
    + [
        P_P_DST / AVG_WALKING_SPEED,
        *[(P_PB_DST + i * PB_PB_DST) / AVG_WALKING_SPEED for i in range(6)],
    ]
)

# Origin-destination pairs
origins = ["105"]
destinations = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]


# Demand between each OD pair (Conjugated to the Cartesian
# product of Origins and destinations with order)
same_platform = (16000 / 13) * (70 / 100)
diff_platform = (16000 / 13) * (30 / 100)

demand = []
for i in range(len(origins)):
    for j in range(len(destinations)):
        if i > j:
            demand.append(0)
        elif i == j:
            demand.append(same_platform)
        else:
            demand.append(diff_platform / (len(destinations) - i - 1))

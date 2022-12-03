# A, X - 1 - Rock,
# B, Y - 2 - Paper,
# C, Z - 3 - Scizzors
# 0 - Lost
# 3 - Draw
# 6 - Win

SHAPE_POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

LOST = 0
DRAW = 3
WIN = 6

COMBINATIONS = {
    "A X": [DRAW, LOST, "Z"],
    "B X": [LOST, LOST, "X"],
    "C X": [WIN, LOST, "Y"],
    "A Y": [WIN, DRAW, "X"],
    "B Y": [DRAW, DRAW, "Y"],
    "C Y": [LOST, DRAW, "Z"],
    "A Z": [LOST, WIN, "Y"],
    "B Z": [WIN, WIN, "Z"],
    "C Z": [DRAW, WIN, "X"],
}

with open("2/input.dat", "r") as fp:
    total_score_1 = 0
    total_score_2 = 0
    for line in fp.readlines():
        total_score_1 += SHAPE_POINTS[line.strip().split(" ")[1]] + COMBINATIONS[line.strip()][0]
        total_score_2 += COMBINATIONS[line.strip()][1] + SHAPE_POINTS[COMBINATIONS[line.strip()][2]]
        
    print("Score 1:", total_score_1)
    print("Score 2:", total_score_2)
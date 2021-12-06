import itertools
import os

def check_for_bingo(a):
    for x in range(5):
        streak = True
        for y in range(5):
            if boards[a][x][y] is not None:
                streak = False
        if streak:
            return True
    for x in range(5):
        streak = True
        for y in range(5):
            if boards[a][y][x] is not None:
                streak = False
        if streak:
            return True
    return False


def calculate_score(num, a):
    score = 0
    for x, y in itertools.product(range(5), range(5)):
        score += boards[a][x][y] if boards[a][x][y] is not None else 0
    score *= num
    return score

with open("2021/04/input.txt", "r") as f:
    data = f.read().strip().split("\n\n")

numbers = [int(x) for x in data.pop(0).split(",")]
boards = [[[int(z) for z in y.split()] for y in x.split("\n")] for x in data]
score = 0

for x in numbers:
    for a in range(len(boards)):
        for b, c in itertools.product(range(len(boards[0])), range(len(boards[0][0]))):
            if boards[a][b][c] == x:
                boards[a][b][c] = None
    if len(boards) > 1:
        boards_to_keep = list(itertools.filterfalse(check_for_bingo, range(len(boards))))
        boards = [boards[a] for a in boards_to_keep]
    elif check_for_bingo(0):
        score = calculate_score(x, 0)
        break
        
print(score)
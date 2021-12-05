import itertools

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

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n\n")

numbers = [int(x) for x in data.pop(0).split(",")]
boards = [[[int(z) for z in y.split()] for y in x.split("\n")] for x in data]
score = 0

for x in numbers:
    for a in range(len(boards)):
        for b, c in itertools.product(range(len(boards[0])), range(len(boards[0][0]))):
            if boards[a][b][c] == x:
                boards[a][b][c] = None
        if check_for_bingo(a):
            score = calculate_score(x, a)
        if score:
            break
    if score:
        break
print(score)
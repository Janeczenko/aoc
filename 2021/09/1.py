import itertools

with open("2021/09/input.txt", "r") as f:
    data = [tuple([int(y) for y in x]) for x in f.read().strip().splitlines()]

risk_sum = 0
for x, y in itertools.product(range(len(data[0])), range(len(data))):
    if (data[x][y] < data[x-1][y] if x != 0 else True) and (data[x][y] < data[x][y-1] if y != 0 else True) and (data[x][y] < data[x+1][y] if x != len(data[0]) - 1 else True) and (data[x][y] < data[x][y+1] if y != len(data) - 1 else True):
        risk_sum += data[x][y] + 1

print(risk_sum)
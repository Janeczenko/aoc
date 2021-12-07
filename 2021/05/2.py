with open("2021/05/input.txt", "r") as f:
    data = f.read().strip().splitlines()

points = [[tuple(int(z) for z in y.split(",")) for y in x.split(" -> ")] for x in data]

max_x = max([max(x[0][0], x[1][0]) for x in points])
max_y = max([max(x[0][1], x[1][1]) for x in points])

vents = [[0 for y in range(max_x + 1)] for x in range(max_y + 1)]

for a in points:
    x1, y1, x2, y2 = a[0][0], a[0][1], a[1][0], a[1][1]
    if x1 == x2:
        if y1 <= y2:
            for b in range(y1, y2 + 1):
                vents[x1][b] += 1
        else:
            for b in range(y2, y1 + 1):
                vents[x1][b] += 1
    elif y1 == y2:
        if x1 <= x2:
            for b in range(x1, x2 + 1):
                vents[b][y1] += 1
        else:
            for b in range(x2, x1 + 1):
                vents[b][y1] += 1
    elif (x1 > x2) == (y1 > y2):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for b, c in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
            vents[b][c] += 1
    else:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = max(y1, y2), min(y1, y2)
        for b, c in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)):
            vents[b][c] += 1


print(sum([len(list(filter(lambda y: y >= 2, x))) for x in vents]))
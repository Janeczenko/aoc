import itertools

def fold(axis, coordinate):
    global points
    if axis == "x":
        for x, y in itertools.product(range(coordinate + 1, len(points[0])), range(len(points))):
            points[y][x - (2 * (x - coordinate))] = points[y][x - (2 * (x - coordinate))] + points[y][x]
        points = [i[0 : coordinate + 1] for i in points]
    else:
        for x, y in itertools.product(range(len(points[0])), range(coordinate + 1, len(points))):
            points[y - (2 * (y - coordinate))][x] = points[y - (2 * (y - coordinate))][x] + points[y][x]
        points = points[0 : coordinate + 1]
        

with open("2021/13/input.txt", "r") as f:
    data = f.read().strip().replace("\r", "").split("\n\n")

point_list = [[int(y) for y in x.split(",")] for x in data[0].splitlines()]
max_x = 0
max_y = 0
for p in point_list:
    max_x = max(max_x, p[0])
    max_y = max(max_y, p[1])
points = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for p in point_list:
    points[p[1]][p[0]] = 1

instructions = [x.split(" ")[2].split("=") for x in data[1].splitlines()]
for x in instructions:
    x[1] = int(x[1])

for ins in instructions:
    fold(*ins)

for x, y in itertools.product(range(len(points[0])), range(len(points))):
    points[y][x] = "X" if points[y][x] > 0 else "."

with open("2021/13/output.txt", "w") as f:
    for x in points:
        f.write("".join([str(y) for y in x]) + "\n")
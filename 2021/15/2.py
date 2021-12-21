import itertools

def get_surrounding(x, y):
    surr = []
    if x + y == 1:
        surr = [0]
    if x > 0:
        surr.append(computed_paths[y][x -1])
    if y > 0:
        surr.append(computed_paths[y - 1][x])
    return surr if surr else [0]

def get_base_risk(x, y):
    return (grid[x % len(grid[0])][y % len(grid)] + (x // len(grid[0])) + (y // len(grid))) % 10

def compute_distance():
    global computed_paths
    for x, y in itertools.product(range(len(computed_paths[0])), range(len(computed_paths))):
        computed_paths[y][x] = min(get_surrounding(x, y)) + get_base_risk(x, y)


with open("2021/15/testinput.txt", "r") as f:
    grid = [[int(y) for y in list(x)] for x in f.read().strip().splitlines()]

computed_paths = [[0 for _ in range(5 * len(grid[0]))] for _ in range(5 * len(grid))]

compute_distance()

print(computed_paths[-1][-1])

with open("2021/15/test.txt", "w") as f:
    for y in range(len(computed_paths)):
        for x in range(len(computed_paths[0])):
            f.write(f"{get_base_risk(x, y)}")
        f.write("\n")
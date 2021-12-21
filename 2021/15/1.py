import itertools

def get_surrounding(x, y):
    surr = []
    if x > 0:
        surr.append(computed_paths[y][x -1])
    if y > 0:
        surr.append(computed_paths[y - 1][x])
    return surr if surr else [0]

def compute_distance():
    global computed_paths
    for x, y in itertools.product(range(len(grid[0])), range(len(grid))):
        computed_paths[y][x] = min(get_surrounding(x, y)) + grid[y][x]


with open("2021/15/input.txt", "r") as f:
    grid = [[int(y) for y in list(x)] for x in f.read().strip().splitlines()]

grid[0][0] = 0


computed_paths = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

compute_distance()

print(computed_paths[-1][-1])
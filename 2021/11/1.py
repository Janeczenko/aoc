import itertools

def inc_square(y, x):
    pass ### TODO: increment in range y-1, x-1 > y+1, x+1

def flash():
    global flashes
    flashed = [[False for _ in range(len(octopuses[0]))] for _ in range(len(octopuses))]
    flash_change = False
    for y, x in itertools.product(range(len(octopuses)), range(len(octopuses[0]))):
        if octopuses[y][x] >= 10 and not flashed[y][x]:
            flash_change = True
            flashes += 1
            flashed[y][x] = True
            inc_square(y, x)
    yield flash_change



with open("2021/11/input.txt", "r") as f:
    octopuses = [[int(y) for y in list(x)] for x in f.read().strip().splitlines()]


flashes = 0
for _ in range(100):
    octopuses = [[y + 1 for y in x] for x in octopuses]
    while True:
        if not flash():
            break

print(flashes)
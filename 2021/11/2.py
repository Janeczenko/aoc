import itertools

def inc_square(y, x):
    for b, a in itertools.product(range(max(0, y - 1), min(len(octopuses), y + 2)), range(max(0, x - 1), min(len(octopuses[0]), x + 2))):
        octopuses[b][a] += 1

def check_all():
    all_flashed = True
    for y, x in itertools.product(range(len(flashed_array)), range(len(flashed_array[0]))):
        if not flashed_array[y][x]:
            all_flashed = False
            break
    return all_flashed
    


with open("2021/11/input.txt", "r") as f:
    octopuses = [[int(y) for y in list(x)] for x in f.read().strip().splitlines()]

end_row = 0
for n in itertools.count(1):
    if end_row:
        break
    for y, x in itertools.product(range(len(octopuses)), range(len(octopuses[0]))):
        octopuses[y][x] = 0 if octopuses[y][x] >= 10 else octopuses[y][x]
    octopuses = [[y + 1 for y in x] for x in octopuses]
    flashed_array = [[False for _ in x] for x in octopuses]
    while True:
        flashed = False
        for y, x in itertools.product(range(len(octopuses)), range(len(octopuses[0]))):
            if octopuses[y][x] >= 10 and not flashed_array[y][x]:
                flashed_array[y][x] = True
                flashed = True
                inc_square(y, x)
        if not flashed:
            if check_all():
                end_row = n
            break

print(end_row)
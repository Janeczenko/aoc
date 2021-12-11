import itertools

def check_adj(x, y):
    add_nums = []
    if ((data[x][y-1] not in ('X', 0)) if y != 0 else False):
        add_nums.append(data[x][y-1])
    if ((data[x-1][y] not in ('X', 0)) if x != 0 else False):
        add_nums.append(data[x-1][y])
    return add_nums

def replace_num(a, b):
    for x, y in itertools.product(range(len(data)), range(len(data[0]))):
        if(data[x][y] == b):
            data[x][y] = a


with open("2021/09/input.txt", "r") as f:
    data = [[int(y) for y in x] for x in f.read().strip().splitlines()]

for x, y in itertools.product(range(len(data)), range(len(data[0]))):
    data[x][y] = 0 if data[x][y] != 9 else 'X'

i = 1
for x, y in itertools.product(range(len(data)), range(len(data[0]))):
    if data[x][y] == 'X':
        continue
    adj = check_adj(x, y)
    adj.sort()
    if len(adj) == 0:
        data[x][y] = i
        i += 1
    elif len(adj) == 1:
        data[x][y] = adj[0]
    else:
        data[x][y] = adj[0]
        replace_num(adj[1], adj[0])

basins = {}
for x, y in itertools.product(range(len(data)), range(len(data[0]))):
    if data[x][y] == "X":
        continue
    else:
        basins.setdefault(data[x][y], 0)
        basins[data[x][y]] += 1

basin_sizes = list(basins.values())
basin_sizes.sort(reverse=True)

print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
import itertools

def check_adj(x, y):
    add_nums = []
    if ((data[x-1][y] not in ('X', 0)) if x != 0 else False):
        add_nums.append(data[x-1][y])
    if ((data[x][y-1] not in ('X', 0)) if y != 0 else False):
        add_nums.append(data[x][y-1])
    if ((data[x+1][y] not in ('X', 0)) if x != len(data[0]) else False):
        add_nums.append(data[x+1][y])
    if ((data[x][y+1] not in ('X', 0)) if y != len(data) else False):
        add_nums.append(data[x][y+1])
    return add_nums

def replace_num(a, b):
    for x, y in itertools.product(range(len(data[0])), range(len(data))):
        pass
    # TODO: WRITE THE REST OF IT

with open("2021/09/input.txt", "r") as f:
    data = [[int(y) for y in x] for x in f.read().strip().splitlines()]

basins = []

for x, y in itertools.product(range(len(data[0])), range(len(data))):
    data[x][y] = 0 if data[x][y] != 9 else 'X'

i = 1
for x, y in itertools.product(range(len(data[0])), range(len(data))):
    if data[x][y] == 'X':
        continue
    adj = check_adj(x, y)
    if len(adj) == 0:
        data[x][y] = i
        i += 1
    elif len(adj) == 1:
        data[x][y] = adj[1]
    else:
        for z in range(1, len(adj)):
            replace_num(z, adj[0])

# TODO: COMPLETE THIS
def generator():
    i = 0
    while True:
        yield i
        i += 1

def counter():
    i = 0
    while True:
        yield i
        i += 1

def can_revisit(cave):
    return cave.isupper()

def path_creator(num, cave):
    global path_counter
    for next_cave in paths[cave]:
        if next_cave not in visited[num] or can_revisit(next_cave):
            if next_cave == "end":
                next(counter())
                break
            visited[num].append(next_cave)
            next_num = generator()
            visited[next_num] = visited[num].copy()
            path_creator(next_num, next_cave)
    else:
        return None

with open("2021/12/input.txt", "r") as f:
    data =  [x.split("-") for x in f.read().strip().splitlines()]


visited = {}
path_counter = 0
paths = {}
for x, y in data:
    if x in paths.keys():
        paths[x].append(y)
    else:
        paths[x] = [y]
    if y in paths.keys():
        paths[y].append(x)
    else:
        paths[y] = [x]

visited[0] = ["start"]
path_creator(next(generator()), "start")

print(next(counter()))

# first, visited[gen] is generated
# visited[gen] gets appended with lowercase caves
# if there are no unvisited/large caves around, break
# if reaches end, path_counter += 1 
import itertools

def can_revisit(num, cave):
    if cave == "start":
        return False
    elif cave.isupper():
        return True
    else:
        return len(visited[num]) == len(set(visited[num]))

def path_creator(num, cave):
    global path_counter
    for next_cave in paths[cave]:
        if next_cave not in visited[num] or can_revisit(num, next_cave):
            if next_cave == "end":
                debug.append(visited[num])
                next(counter)
                continue
            next_num = next(generator)
            visited[next_num] = visited[num].copy()
            if not next_cave.isupper():
                visited[next_num].append(next_cave)
            path_creator(next_num, next_cave)
    else:
        return

with open("2021/12/input.txt", "r") as f:
    data =  [x.split("-") for x in f.read().strip().splitlines()]

debug = []

generator = itertools.count()
counter = itertools.count()
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
path_creator(next(generator), "start")

print(next(counter))
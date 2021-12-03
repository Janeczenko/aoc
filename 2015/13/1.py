import itertools

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")

data = [x.split() for x in data]
data = [[x[0], (1 if x[2] == "gain" else -1) * int(x[3]), x[-1][:-1]] for x in data]

names = set([x[0] for x in data])

max_happiness = 0
for i in itertools.permutations(names):
    happiness = 0
    for j in range(len(i)):
        for d in data:
            if (d[0] == i[j] and d[2] == i[(j + 1) % len(i)]) or (d[0] == i[(j + 1) % len(i)] and d[2] == i[j]):
                happiness += d[1]
    max_happiness = max(max_happiness, happiness)
    

print(max_happiness)
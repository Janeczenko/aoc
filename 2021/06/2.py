import collections

with open("2021/06/input.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split(",")]

fish = dict(collections.Counter(data))
print(fish)

for _ in range(256):
    fish_tmp = {}
    for x in fish.keys():
        if x == 0:
            fish_tmp[8] = fish[x]
            fish_tmp[6] = fish[x] if 6 not in fish_tmp.keys() else fish_tmp[6] + fish[x]
        else:
            fish_tmp[x - 1] = fish[x] if (x - 1) not in fish_tmp.keys() else fish_tmp[x - 1] + fish[x]
    fish = fish_tmp


print(sum(fish.values()))
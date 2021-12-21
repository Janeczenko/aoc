import collections
import math


def extend_polymer():
    global pairs
    new_dict = {}
    for pair, quant in pairs.items():
        ins = codes[pair]
        new_1 = pair[0] + ins
        new_2 = ins + pair[1]
        new_dict.setdefault(new_1, 0)
        new_dict.setdefault(new_2, 0)
        new_dict[new_1] += quant
        new_dict[new_2] += quant
    pairs = new_dict.copy()

def count_occurences():
    occurences = {}
    for k, v in pairs.items():
        occurences.setdefault(k[0], 0)
        occurences.setdefault(k[1], 0)
        occurences[k[0]] += v
        occurences[k[1]] += v
    for k, v in occurences.items():
        occurences[k] = math.ceil(v / 2)
    return max(occurences.values()) - min(occurences.values())


with open("2021/14/input.txt", "r") as f:
    data = f.read().strip().replace("\r", "").split("\n\n")

polymer = list(data[0])
pairs = dict(collections.Counter([polymer[i] + polymer[i + 1] for i in range(len(polymer) - 1)]))

codes = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in data[1].splitlines()}


for i in range(40):
    extend_polymer()

print(count_occurences())
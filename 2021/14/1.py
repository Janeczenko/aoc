def extend_polymer():
    insertions = []
    for i in range(len(polymer) - 1):
        insertions.append(codes[f"{polymer[i]}{polymer[i+1]}"])
    for i in range(len(insertions)):
        polymer.insert((2 * i) + 1, insertions[i])


def count_occurences():
    occs = {}
    for p in polymer:
        occs.setdefault(p, 0)
        occs[p] += 1
    
    return max(occs.values()) - min(occs.values())



with open("2021/14/input.txt", "r") as f:
    data = f.read().strip().replace("\r", "").split("\n\n")

polymer = list(data[0])

codes = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in data[1].splitlines()}


for i in range(10):
    print(f"Step {i + 1}")
    extend_polymer()

print(count_occurences())
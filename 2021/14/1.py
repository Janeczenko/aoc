def extend_polymer():
    insertions = []
    for i in range(len(polymer) - 1):
        pass

with open("2021/14/input.txt", "r") as f:
    data = f.read().strip().replace("\r", "").split("\n\n")

polymer = list(data[0])

codes = [x.split(" -> ") for x in data[1].splitlines()]

for _ in range(10):
    extend_polymer()
with open("2021/08/input.txt", "r") as f:
    data = [[tuple(y.strip().split(" ")) for y in x.split("|")] for x in f.read().strip().splitlines()]

digits = 0
for x in data:
    digits += len([y for y in x[1] if len(y) in (2, 3, 4, 7)])

print(digits)
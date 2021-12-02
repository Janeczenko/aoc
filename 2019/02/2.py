import itertools 

with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split(",")]

for i, j in itertools.product(range(100), range(100)):
    data_copy = data.copy()
    data_copy[1] = i
    data_copy[2] = j
    for k in range(0, len(data_copy), 4):
        if data_copy[k] == 1:
            data_copy[data_copy[k + 3]] = data_copy[data_copy[k + 1]] + data_copy[data_copy[k + 2]]
        elif data_copy[k] == 2:
            data_copy[data_copy[k + 3]] = data_copy[data_copy[k + 1]] * data_copy[data_copy[k + 2]]
        elif data_copy[k] == 99:
            break
    if data_copy[0] == 19690720:
        break

print(100 * i + j)
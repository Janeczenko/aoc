with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split(",")]

data[1] = 12
data[2] = 2

for i in range(0, len(data), 4):
    if data[i] == 1:
        data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
    elif data[i] == 2:
        data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
    elif data[i] == 99:
        break

print(data[0])
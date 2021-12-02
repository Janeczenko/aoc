with open("input.txt", "r") as f:
    data = []
    while(row := f.readline()):
        row = row.replace("\n", "").split()
        data.append(row)

depth = 0
position = 0
aim = 0

for i in data:
    if i[0] == "forward":
        position += int(i[1])
        depth += aim * int(i[1])
    elif i[0] == "down":
        aim += int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])


print(depth * position)
with open("2021/03/input.txt", "r") as f:
    data = f.read().strip().split("\n")
    
gamma = ""
epsilon = ""
for i in range(len(data[0])):
    count_0 = 0
    count_1 = 0
    for j in range(len(data)):
        if data[j][i] == "0":
            count_0 += 1
        else:
            count_1 += 1
    gamma += "0" if count_0 > count_1 else "1"
    epsilon += "1" if count_0 > count_1 else "0"

print(int(gamma, 2) * int(epsilon, 2))
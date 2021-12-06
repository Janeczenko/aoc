with open("2021/01/input.txt", "r") as f:
    data = []
    while(row := f.readline()):
        row = row.replace("\n", "")
        data.append(row)

    timesIncreased = 0
    for i in range(1, len(data)):
        if int(data[i])>int(data[i-1]): timesIncreased += 1

    print(timesIncreased)
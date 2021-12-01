with open("input.txt", "r") as f:
    data = []
    while(row := f.readline()):
        data.append(row)

    timesIncreased = 0
    for i in range(1, len(data)):
        if data[i]>data[i-1]: timesIncreased += 1

    print(timesIncreased)
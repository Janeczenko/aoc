with open("input.txt", "r") as f:
    data = []
    while(row := f.readline()):
        row = int(row.replace("\n", ""))
        data.append(row)

    timesIncreased = 0
    previousSum = 0
    currentSum = 0
    for i in range(2, len(data)):
        previousSum = currentSum
        currentSum = data[i] + data[i-1] + data[i-2]
        if previousSum and currentSum and currentSum > previousSum: timesIncreased += 1

    print(timesIncreased)
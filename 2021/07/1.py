import statistics

with open("2021/07/input.txt", "r") as f:
    positions = [int(x) for x in f.read().strip().split(",")]
    positions.sort()

median = int(statistics.median(positions))

fuel = sum([abs(median - x) for x in positions])
print(fuel)
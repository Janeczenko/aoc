with open("2021/07/input.txt", "r") as f:
    positions = [int(x) for x in f.read().strip().split(",")]
    positions.sort()

# Fuel cost: (x^2 + x) / 2
with open("2021/07/input.txt", "r") as f:
    positions = [int(x) for x in f.read().strip().split(",")]
    positions.sort()

min_fuel = 0
for x in range(min(positions), max(positions)):
    fuel = 0
    for y in positions:
        diff = abs(x - y)
        fuel += int((diff**2 + diff) / 2)
    min_fuel = min(min_fuel, fuel) if min_fuel else fuel

print(min_fuel)

# Fuel cost: (x^2 + x) / 2
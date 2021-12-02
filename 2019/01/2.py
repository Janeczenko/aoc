import math

def calc_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)


with open("input.txt", "r") as f:
    data = f.read().split("\n")
data.pop()

fuel_needed = 0
for i in data:
    fuel_needed += calc_fuel(int(i))

print(fuel_needed)

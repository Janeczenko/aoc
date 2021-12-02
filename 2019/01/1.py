import math

with open("input.txt", "r") as f:
    data = f.read().split("\n")
data.pop()

fuel_needed = 0
for i in data:
    fuel_needed += math.floor(int(i) / 3) - 2

print(fuel_needed)
from os import stat
import statistics

with open("2021/10/input.txt", "r") as f:
    data = f.read().strip().splitlines()

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
scoring = {")": 1, "]": 2, "}": 3, ">": 4}
points = []
for line in data:
    broken = False
    stack = []
    for bracket in line:
        if bracket in "([{<":
            stack.append(bracket)
        elif bracket != pairs[stack.pop()]:
            broken = True
            break
    if broken:
        continue
    points_tmp = 0
    stack.reverse()
    for bracket in stack:
        points_tmp *= 5
        points_tmp += scoring[pairs[bracket]]
    points.append(points_tmp)

print(statistics.median(points))
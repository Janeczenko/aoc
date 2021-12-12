with open("2021/10/input.txt", "r") as f:
    data = f.read().strip().splitlines()

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
points = 0
for line in data:
    stack = []
    for bracket in line:
        if bracket in "([{<":
            stack.append(bracket)
        elif bracket != pairs[stack.pop()]:
            points += scoring[bracket]
            break

print(points)
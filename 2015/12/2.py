import json
import re


def check_dict(d):
    for x, y in d.items():
        if y == "red":
            d.clear()
            break
        if isinstance(y, dict):
            check_dict(y)
        elif isinstance(y, list):
            check_list(y)

def check_list(l):
    for x in l:
        if isinstance(x, dict):
            check_dict(x)
        elif isinstance(x, list):
            check_list(x)


with open('input.txt', 'r') as f:
    data = json.load(f)


check_dict(data)

data_string = json.dumps(data)
numbers = list(map(lambda x: int(x), re.findall(r'-?\d+', data_string)))
print(sum(numbers))
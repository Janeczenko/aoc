import re


with open('input.txt', 'r') as file:
    input = file.read()
    numbers = list(map(lambda x: int(x),re.findall(r'-?\d+',input)))
    print(sum(numbers))
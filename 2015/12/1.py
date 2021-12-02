import os
import re


with open(os.path.join(os.getcwd(),'12','input.txt')) as file:
    input = file.read()
    numbers = list(map(lambda x: int(x),re.findall(r'-?\d+',input)))
    print(sum(numbers))
import os
import itertools

with open('input.txt', 'r') as file:
    input = file.read()
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for line in input.split('\n'):
        parameters = line.replace(' ',',').split(',')
        if parameters[0] == 'turn':
            parameters.pop(0)
        if parameters[0] == 'on':
            for x, y in itertools.product(range(int(parameters[1]),int(parameters[4])+1), range(int(parameters[2]),int(parameters[5])+1)):
                lights[x][y] = 1
        elif parameters[0] == 'off':
            for x, y in itertools.product(range(int(parameters[1]),int(parameters[4])+1), range(int(parameters[2]),int(parameters[5])+1)):
                lights[x][y] = 0
        elif parameters[0] == 'toggle':
            for x, y in itertools.product(range(int(parameters[1]),int(parameters[4])+1), range(int(parameters[2]),int(parameters[5])+1)):
                lights[x][y] = 0 if lights[x][y] == 1 else 1
    print(sum(row.count(1) for row in lights))
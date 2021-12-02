import os
import itertools

with open(os.path.join(os.getcwd(),'06','input.txt')) as file:
    input = file.read()
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for line in input.split('\n'):
        parameters = line.replace(' ',',').split(',')
        if parameters[0] == 'turn':
            parameters.pop(0)
        if parameters[0] == 'on':
            for x, y in itertools.product(range(int(parameters[1]),int(parameters[4])+1), range(int(parameters[2]),int(parameters[5])+1)):
                lights[x][y] += 1
        elif parameters[0] == 'off':
            for x, y in itertools.product(range(int(parameters[1]),int(parameters[4])+1), range(int(parameters[2]),int(parameters[5])+1)):
                lights[x][y] = max(0,lights[x][y]-1)
        elif parameters[0] == 'toggle':
            for x, y in itertools.product(range(int(parameters[1]),int(parameters[4])+1), range(int(parameters[2]),int(parameters[5])+1)):
                lights[x][y] +=2
    print(sum(sum(row) for row in lights))
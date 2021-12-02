import os
import itertools

def findSinglePath(city1, city2):
    global paths
    for path in paths:
        if city1 in path and city2 in path:
            return int(path[2])


with open(os.path.join(os.getcwd(),'09','input.txt')) as file:
    paths = file.read().replace('\n',' = ').replace('to','=').split(' = ')
    paths = [paths[i:i+3] for i in range(0,len(paths),3)]
    cities = set()
    for i in paths:
        for j in range(0,2):
            cities.add(i[j])

    path_lengths = []
    for perm in list(itertools.permutations(cities)):
        path_len = 0
        for i in range(1,len(perm)):
            path_len += findSinglePath(perm[i-1],perm[i])
        path_lengths.append(path_len)
    print(max(path_lengths))
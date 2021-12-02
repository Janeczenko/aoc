import os

with open(os.path.join(os.getcwd(),'05','input.txt')) as file:
    input = file.read().split('\n')
    num_nice = 0
    for line in input:
        two_pairs = False
        oreo = False
        for i in range(len(line)-1):
            for j in range(i+2,len(line)-1):
                if line[i:i+2] == line[j:j+2]:
                    two_pairs = True
        for i in range(1, len(line)-1):
            if line[i-1] == line[i+1]:
                oreo = True
        if two_pairs and oreo:
            num_nice += 1
    print(num_nice)
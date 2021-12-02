import os

with open(os.path.join(os.getcwd(),'02','input.txt')) as file:
    ft = 0
    while True:
        line = file.readline().replace('\n','')
        if not line:
            break
        box = line.split('x')
        l = int(box[0])
        w = int(box[1])
        h = int(box[2])
        ft += 2*(l+w+h) - 2*max(l,w,h) + l*w*h
    print(ft)
        
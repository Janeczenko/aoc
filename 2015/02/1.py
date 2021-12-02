import os

with open(os.path.join(os.getcwd(),'02','input.txt')) as file:
    sqr_ft = 0
    while True:
        line = file.readline().replace('\n','')
        if not line:
            break
        box = line.split('x')
        l = int(box[0])
        w = int(box[1])
        h = int(box[2])
        sqr_ft += 2*l*w + 2*l*h + 2*w*h + min(l*w,l*h,w*h)
    print(sqr_ft)
        
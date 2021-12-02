import os

with open(os.path.join(os.getcwd(),'01','input.txt')) as file:
    floor = 0
    file_content = file.read()
    for i in range(len(file_content)):
        if file_content[i] == '(':
            floor+=1
        else:
            floor-=1
        if floor<0:
            print(i+1)
            break
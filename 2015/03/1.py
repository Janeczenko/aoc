import os

with open(os.path.join(os.getcwd(),'03','input.txt')) as file:
    coord_vis = [[0,0]]
    coord_cur = [0,0]
    for direction in file.read():
        if direction == '^':
            coord_cur[1] += 1
        elif direction == '>':
            coord_cur[0] += 1
        elif direction == 'v':
            coord_cur[1] -= 1
        else:
            coord_cur[0] -= 1
        if not coord_cur in coord_vis:
            coord_vis.append(coord_cur.copy())
    print(len(coord_vis))

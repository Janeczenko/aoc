import os

with open(os.path.join(os.getcwd(),'03','input.txt')) as file:
    coord_vis = [[0,0]]
    coord_cur = [[0,0],[0,0]]
    for index, direction in enumerate(file.read()):
        if direction == '^':
            coord_cur[index%2][1] += 1
        elif direction == '>':
            coord_cur[index%2][0] += 1
        elif direction == 'v':
            coord_cur[index%2][1] -= 1
        else:
            coord_cur[index%2][0] -= 1
        if not coord_cur[index%2] in coord_vis:
            coord_vis.append(coord_cur[index%2].copy())
    print(len(coord_vis))

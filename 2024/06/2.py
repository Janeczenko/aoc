import itertools
import copy

def possible_locations():
    with open('input.txt', 'r') as f:
        map_rows = f.read().strip().split()
    map_list = [list(row) for row in map_rows]

    for i in range(len(map_list)):
        if '^' in map_list[i]:
            guard_pos = [i, map_list[i].index('^')]
    
    guard_dir = 'u'
    
    map_list[guard_pos[0]][guard_pos[1]] = 'X'
    while True:
        if guard_pos[0] < 0 or guard_pos[0] >= len(map_list) or guard_pos[1] < 0 or guard_pos[1] >= len(map_list[1]):
            break
        map_list[guard_pos[0]][guard_pos[1]] = 'X'
        match guard_dir:
            case 'u':
                if map_list[guard_pos[0]-1][guard_pos[1]] != '#':
                    guard_pos[0] -= 1
                else:
                    guard_dir = 'r'
            case 'r':
                if map_list[guard_pos[0]][guard_pos[1]+1] != '#':
                    guard_pos[1] += 1
                else:
                    guard_dir = 'd'
            case 'd':
                if map_list[guard_pos[0]+1][guard_pos[1]] != '#':
                    guard_pos[0] += 1
                else:
                    guard_dir = 'l'
            case 'l':
                if map_list[guard_pos[0]][guard_pos[1]-1] != '#':
                    guard_pos[1] -= 1
                else:
                    guard_dir = 'u'
    
    output = []
    for i,j in itertools.product(range(len(map_list)), range(len(map_list[0]))):
        if map_list[i][j] == 'X':
            output.append((i,j))
    
    return output

def main():
    with open('input.txt', 'r') as f:
        map_rows = f.read().strip().split()
    map_list = [list(row) for row in map_rows]

    for i in range(len(map_list)):
        if '^' in map_list[i]:
            guard_pos = [i, map_list[i].index('^')]
    
    counter = 0

    for (i,j) in possible_locations():
        if map_list[i][j] == '^':
            continue
        
        map_list_copy = copy.deepcopy(map_list)
        map_list_copy[i][j] = '#'
        guard_path = list()
        guard_pos_copy = copy.deepcopy(guard_pos)
        guard_dir = 'u'
        looped = True

        while (tuple(guard_pos_copy), guard_dir) not in guard_path:
            guard_path.append((tuple(guard_pos_copy), guard_dir))
            map_list_copy[guard_pos_copy[0]][guard_pos_copy[1]] = 'X'
            match guard_dir:
                case 'u':
                    if guard_pos_copy[0] <= 0:
                        looped = False
                        break
                    if map_list_copy[guard_pos_copy[0]-1][guard_pos_copy[1]] != '#':
                        guard_pos_copy[0] -= 1
                    else:
                        guard_dir = 'r'
                case 'r':
                    if guard_pos_copy[1] >= len(map_list_copy[0]) - 1:
                        looped = False
                        break
                    if map_list_copy[guard_pos_copy[0]][guard_pos_copy[1]+1] != '#':
                        guard_pos_copy[1] += 1
                    else:
                        guard_dir = 'd'
                case 'd':
                    if guard_pos_copy[0] >= len(map_list_copy) - 1:
                        looped = False
                        break
                    if map_list_copy[guard_pos_copy[0]+1][guard_pos_copy[1]] != '#':
                        guard_pos_copy[0] += 1
                    else:
                        guard_dir = 'l'
                case 'l':
                    if guard_pos_copy[1] <= 0:
                        looped = False
                        break
                    if map_list_copy[guard_pos_copy[0]][guard_pos_copy[1]-1] != '#':
                        guard_pos_copy[1] -= 1
                    else:
                        guard_dir = 'u'
        
        if looped:
            counter += 1

    print(counter)

if __name__ == '__main__':
    main()
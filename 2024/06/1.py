def main():
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
    
    total_visited = sum([len(list(filter(lambda x: x == 'X', row))) for row in map_list])
    print(total_visited)

if __name__ == '__main__':
    main()
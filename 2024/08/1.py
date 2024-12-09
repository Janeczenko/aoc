import itertools

def main():
    with open('test.txt', 'r') as f:
        map_rows = f.read().strip().split()
    
    antennas = dict()
    map_height = len(map_rows)
    map_width = len(map_rows[0])

    for i in range(map_height):
        for j in range(map_width):
            cur_char = map_rows[i][j]
            if cur_char == '.':
                continue
            elif cur_char in antennas.keys():
                antennas[cur_char].append((i,j))
            else:
                antennas[cur_char] = [(i,j)]
    
    for (freq, coords) in antennas.items():
        for ((a,b), (c,d)) in itertools.combinations(coords, 2):
            diff_1 = c - a
            diff_2 = d - b



if __name__ == '__main__':
    main()
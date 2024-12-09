import itertools

def main():
    with open('input.txt', 'r') as f:
        map_rows = f.read().strip().split()
    
    antennas = dict()
    map_height = len(map_rows)
    map_width = len(map_rows[0])
    antinode_locations = [[0 for _ in range(map_width)] for _ in range(map_height)]

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
            if 0 <= c + diff_1 < map_height and 0 <= d + diff_2 < map_width:
                antinode_locations[c + diff_1][d + diff_2] = 1
            if 0 <= a - diff_1 < map_height and 0 <= b - diff_2 < map_width:
                antinode_locations[a - diff_1][b - diff_2] = 1

    antinode_location_count = sum([sum(r) for r in antinode_locations])
    print(antinode_location_count)
            


if __name__ == '__main__':
    main()
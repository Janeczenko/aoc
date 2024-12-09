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
            (e, f) = (c, d)
            while 0 <= e < map_height and 0 <= f < map_width:
                antinode_locations[e][f] = 1
                (e, f) = (e + diff_1, f + diff_2)
            (e, f) = (a, b)
            while 0 <= e < map_height and 0 <= f < map_width:
                antinode_locations[e][f] = 1
                (e, f) = (e - diff_1, f - diff_2)

    antinode_location_count = sum([sum(r) for r in antinode_locations])
    print(antinode_location_count)
            


if __name__ == '__main__':
    main()
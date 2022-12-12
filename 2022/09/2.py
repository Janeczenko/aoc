def move_knot(rope:list[tuple[int]], num:int, direction:tuple[int])->None:
    if abs(rope[num-1][0] - rope[num][0]) > 1:
        rope[num][0] += (rope[num-1][0] - rope[num][0])//2
        rope[num][1] += int(rope[num][1] != rope[num-1][1]) * (-1 if rope[num-1][1] < rope[num][1] else 1)
    elif abs(rope[num-1][1] - rope[num][1]) > 1:
        rope[num][1] += (1 if rope[num-1][1] > rope[num][1] else -1)
        rope[num][0] = rope[num-1][0]
    return None


def simulate_motion(visited:list[tuple[int]], rope:list[tuple[int]], com:tuple)->None:
    motion_visited = [tuple(rope[9])]
    directions = {'U':(0, 1), 'D':(0, -1), 'L':(1, -1), 'R':(1, 1)}
    for _ in range(com[1]):
        direction = directions[com[0]]
        rope[0][direction[0]] += direction[1]
        for knot_number in range(1, len(rope)):
            move_knot(rope, knot_number, direction)
        motion_visited.append(tuple(rope[9]))
    visited.extend(motion_visited)
    return None


def main():
    with open('input.txt', 'r') as f:
        commands = [x.split() for x in f.read().strip().split('\n')]
    positions_visited_by_tail = []
    rope_position = [[0, 0] for _ in range(10)]
    for command in commands:
        command[1] = int(command[1])
        simulate_motion(positions_visited_by_tail, rope_position, command)
        positions_visited_by_tail = list(set(positions_visited_by_tail))
    print(len(positions_visited_by_tail))


if __name__ == '__main__':
    main()
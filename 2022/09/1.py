def simulate_motion(visited:list[tuple[int]], head:tuple[int], tail:tuple[int], com:tuple)->None:
    motion_visited = [tuple(tail)]
    directions = {'U':(0, 1), 'D':(0, -1), 'L':(1, -1), 'R':(1, 1)}
    for _ in range(com[1]):
        head[directions[com[0]][0]] += directions[com[0]][1]
        if abs(head[0] - tail[0]) > 1:
            tail[0] += directions[com[0]][1]
            tail[1] = head[1]
        elif abs(head[1] - tail[1]) > 1:
            tail[1] += directions[com[0]][1]
            tail[0] = head[0]
        motion_visited.append(tuple(tail))
    visited.extend(motion_visited)
    return None


def main():
    with open('input.txt', 'r') as f:
        commands = [x.split() for x in f.read().strip().split('\n')]
    positions_visited_by_tail = []
    head_position = [0, 0]
    tail_position = [0, 0]
    for command in commands:
        command[1] = int(command[1])
        simulate_motion(positions_visited_by_tail, head_position, tail_position, command)
        positions_visited_by_tail = list(set(positions_visited_by_tail))
    print(len(positions_visited_by_tail))


if __name__ == '__main__':
    main()
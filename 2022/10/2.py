def main():
    with open('input.txt', 'r') as f:
        lines = [x.split(' ') for x in f.read().strip().split('\n')]
    for x in lines:
        if len(x) > 1:
            x[1] = int(x[1])

    register_x = 1
    instruction_index = 0
    addx_value = 0
    addx_on_next_cycle = False
    crt = [None for _ in range(240)]

    for cycle_num in range(240):
        crt[cycle_num] = '#' if abs(register_x - cycle_num % 40) <= 1 else '.'
        if addx_on_next_cycle:
            addx_on_next_cycle = False
            register_x += addx_value
            instruction_index += 1
        elif lines[instruction_index][0] == 'noop':
            instruction_index += 1
        else:
            addx_value = lines[instruction_index][1]
            addx_on_next_cycle = True

    crt_split = [crt[40*i:40*i+40] for i in range(6)]
    for row in crt_split:
        print(''.join(row))



if __name__ == '__main__':
    main()
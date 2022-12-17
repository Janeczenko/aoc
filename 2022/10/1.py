def main():
    with open('input.txt', 'r') as f:
        lines = [x.split(' ') for x in f.read().strip().split('\n')]
    for x in lines:
        if len(x) > 1:
            x[1] = int(x[1])

    register_x = 1
    signal_sum = 0
    instruction_index = 0
    addx_value = 0
    addx_on_next_cycle = False

    for cycle_num in range(1, 221):
        if cycle_num % 40 == 20:
            signal_sum += cycle_num * register_x
        if addx_on_next_cycle:
            addx_on_next_cycle = False
            register_x += addx_value
            instruction_index += 1
        elif lines[instruction_index][0] == 'noop':
            instruction_index += 1
        else:
            addx_value = lines[instruction_index][1]
            addx_on_next_cycle = True

    print(signal_sum)


if __name__ == '__main__':
    main()
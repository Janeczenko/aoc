import re


def main():
    with open('input.txt', 'r') as f:
        crates, instructions = list(re.split(r'\n[\s0123456789]+\n', str(f.read().strip('\n'))))

    crates_matrix = [[] for _ in range(len(crates.split('\n')[-1].split(' ')))]
    for i, x in enumerate(crates.split('\n')[::-1]):
        for j, y in enumerate(range(1, len(x), 4)):
            if x[y] != ' ':
                crates_matrix[j].append(x[y])

    instructions_matrix = [[int(y) for y in re.findall(r'\d+', x)] for x in instructions.split('\n')]

    for instruction in instructions_matrix:
        amount, origin, destination = instruction
        origin -= 1
        destination -= 1
        for _ in range(amount):
            crates_matrix[destination].append(crates_matrix[origin].pop())

    print(''.join([x[-1] for x in crates_matrix]))


if __name__ == '__main__':
    main()
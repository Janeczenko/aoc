import re

def main():
    with open('input.txt', 'r') as f:
        command_list = f.read().strip().split()

    score = 0
    for command in command_list:
        mul_nums = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', command)
        score += sum([int(mul[0])*int(mul[1]) for mul in mul_nums])
    print(score)

if __name__ == '__main__':
    main()
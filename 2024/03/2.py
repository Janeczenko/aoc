import re

def main():
    with open('input.txt', 'r') as f:
        command_list = f.read().strip().split()

    score = 0
    count_muls = True
    for command in command_list:
        words_found = re.findall(r'(do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\))', command)
        for word in words_found:
            match word[:3]:
                case 'do(':
                    count_muls = True
                case 'don':
                    count_muls = False
                case 'mul':
                    if count_muls:
                        nums = re.findall(r'\d+', word)
                        score += int(nums[0])*int(nums[1])
    print(score)

if __name__ == '__main__':
    main()
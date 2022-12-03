def main():
    with open('input.txt', 'r') as f:
        lines = [x for x in f.read().strip().split('\n')]
    groups = [(set(lines[3*x]), set(lines[3*x+1]), set(lines[3*x+2])) for x in range(len(lines)//3)]
    sum = 0
    for x in groups:
        common_item = list(x[0].intersection(x[1]).intersection(x[2]))[0]
        sum += ord(common_item) - (38 if common_item.upper() == common_item else 96)
    print(sum)


if __name__ == '__main__':
    main()
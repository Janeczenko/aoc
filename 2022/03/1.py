def main():
    with open('input.txt', 'r') as f:
        lines = [x for x in f.read().strip().split('\n')]
    rucksacks = [(set(x[:len(x)//2]), set(x[len(x)//2:])) for x in lines]
    sum = 0
    for x in rucksacks:
        common_item = list(x[0].intersection(x[1]))[0]
        sum += ord(common_item) - (38 if common_item.upper() == common_item else 96)
    print(sum)


if __name__ == '__main__':
    main()
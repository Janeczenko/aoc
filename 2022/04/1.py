def main():
    with open('input.txt', 'r') as f:
        lines = [x for x in f.read().strip().split('\n')]
    pairs_list = [[[int(z) for z in y.split('-')] for y in x.split(',')] for x in lines]
    overlapping_pair_amount = 0
    for x in pairs_list:
        if (x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) or (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]):
            overlapping_pair_amount += 1
    print(overlapping_pair_amount)


if __name__ == '__main__':
    main()
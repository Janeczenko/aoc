def main():
    with open('input.txt', 'r') as f:
        elves_food = f.read().strip().split('\n\n')
    elves_food_tables = [[int(y) for y in x.strip().split('\n')] for x in elves_food]
    elves_food_sums = [sum(x) for x in elves_food_tables]

    print(max(elves_food_sums))


if __name__ == '__main__':
    main()
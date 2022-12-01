def main():
    with open('input.txt', 'r') as f:
        elves_food = f.read().strip().split('\n\n')
    elves_food_tables = [[int(y) for y in x.strip().split('\n')] for x in elves_food]
    elves_food_sums = [sum(x) for x in elves_food_tables]
    elves_food_sums.sort()
    print(elves_food_sums[-1] + elves_food_sums[-2] + elves_food_sums[-3])


if __name__ == '__main__':
    main()
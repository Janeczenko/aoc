def calc_diff(a, b):
    for x in b:
        if x not in a:
            return False
    return "".join([x for x in a if x not in b])

def decode_numbers(translation, output):
    numbers = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

    decoder = {y:x for x, y in translation.items()}

    decoded_output = []
    for x in output:
        decoded_num = "".join([decoder[y] for y in x])
        for y in numbers:
            if calc_diff(decoded_num, y) == "":
                decoded_output.append(numbers.index(y))

    return decoded_output

def calculate_output(row):
    code = row[0]
    output = row[1]
    translation = {}

    one = "".join([x for x in code if len(x) == 2])
    seven = "".join([x for x in code if len(x) == 3])
    four = "".join([x for x in code if len(x) == 4])
    two_three_five = [x for x in code if len(x) == 5]
    zero_six_nine = [x for x in code if len(x) == 6]
    eight = "".join([x for x in code if len(x) == 7])

    # 7-1=a -> a
    translation["a"] = calc_diff(seven, one)
    # 9-4-a=g -> g
    for x in zero_six_nine:
        subtraction = calc_diff(x, four + translation["a"])
        if subtraction is not False and len(subtraction) == 1:
            nine = x
            translation["g"] = subtraction
            break
    #3-1-a-g=d -> d
    for x in two_three_five:
        subtraction = calc_diff(x, one + translation["a"] + translation["g"])
        if subtraction is not False and len(subtraction) == 1:
            translation["d"] = subtraction
            break
    # 8-6=c -> c ### must be in 1
    for x in zero_six_nine:
        subtraction = calc_diff(eight, x)
        if subtraction is not False and len(subtraction) == 1 and subtraction in one:
            translation["c"] = subtraction
            break
    # 1-c=f -> f
    translation["f"] = calc_diff(one, translation["c"])
    # 9-3=b -> b
    translation["b"] = calc_diff(four, one + translation["d"])
    # 9-8=e -> e
    translation["e"] = calc_diff(eight, nine)

    decoded_numbers = decode_numbers(translation, output)
    return 1000 * decoded_numbers[0] + 100 * decoded_numbers[1] + 10 * decoded_numbers[2] + decoded_numbers[3]

with open("2021/08/input.txt", "r") as f:
    data = [[tuple(y.strip().split(" ")) for y in x.split("|")] for x in f.read().strip().splitlines()]


print(sum([calculate_output(x) for x in data]))
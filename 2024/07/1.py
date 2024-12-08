import itertools

def main():
    with open('input.txt', 'r') as f:
        equations = f.read().strip().split('\n')
    equations = [e.replace(':', '').split() for e in equations]

    total = 0
    for eq in equations:
        eq = list(map(int, eq))
        is_correct = False
        for sign_var in itertools.product((0, 1), repeat=len(eq)-2):
            # 0 means +, 1 means *
            result = eq[1]
            for i in range(2, len(eq)):
                result = result * eq[i] if sign_var[i-2] else result + eq[i]
            if result == eq[0]:
                is_correct = True
                break
        if is_correct:
            total += eq[0]
    
    print(total)

if __name__ == '__main__':
    main()
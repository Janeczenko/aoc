def main():
    with open('input.txt', 'r') as f:
        lines = [x for x in f.read().strip().split('\n')]
    score = 0
    score_table = {'X':0, 'Y':3, 'Z':6}
    abc_table = {'A':1, 'B':2, 'C':3}
    for i in lines:
        score += (abc_table[i[0]] + score_table[i[2]]//3 + 1) % 3 + 1
        score += score_table[i[2]]
    print(score)


if __name__ =='__main__':
    main()

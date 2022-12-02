def main():
    with open('input.txt', 'r') as f:
        lines = [x for x in f.read().strip().split('\n')]
    score = 0
    score_table = {'X':1, 'Y':2, 'Z':3, 'AY':6, 'BZ':6, 'CX':6, 'AX':3, 'BY':3, 'CZ':3, 'AZ':0, 'BX':0, 'CY':0}
    for i in lines:
        score += score_table[i[2]]
        score += score_table[i.replace(' ', '')]
    print(score)


if __name__ =='__main__':
    main()

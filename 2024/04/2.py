def main():
    with open('input.txt', 'r') as f:
        wsr = f.read().strip().split()
    ws = [list(row) for row in wsr]

    height = len(ws)
    width = len(ws[0])

    total = 0
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            if ws[r][c] != 'A':
                continue

            characters = [ws[r-1][c-1], ws[r-1][c+1], ws[r+1][c+1], ws[r+1][c-1]]
            if ''.join(characters) in ('MMSS', 'MSSM', 'SSMM', 'SMMS'):
                total += 1
            
    print(total)

if __name__ == '__main__':
    main()
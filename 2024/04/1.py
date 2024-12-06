def main():
    with open('input.txt', 'r') as f:
        wsr = f.read().strip().split()
    ws = [list(row) for row in wsr]

    height = len(ws)
    width = len(ws[0])

    total = 0
    for r in range(height):
        for c in range(width):
            go_right = c <= width - 4
            go_left = c >= 3
            go_up = r >= 3
            go_down = r <= height - 4
            
            # right directions
            if go_right:
                # right
                if ''.join([ws[r][c], ws[r][c+1], ws[r][c+2], ws[r][c+3]]) == 'XMAS':
                    total += 1
                # up right
                if go_up:
                    if ''.join([ws[r][c], ws[r-1][c+1], ws[r-2][c+2], ws[r-3][c+3]]) == 'XMAS':
                        total += 1
                # down right
                if go_down:
                    if ''.join([ws[r][c], ws[r+1][c+1], ws[r+2][c+2], ws[r+3][c+3]]) == 'XMAS':
                        total += 1

            # left directions
            if go_left:
                # left
                if ''.join([ws[r][c], ws[r][c-1], ws[r][c-2], ws[r][c-3]]) == 'XMAS':
                    total += 1
                # up left
                if go_up:
                    if ''.join([ws[r][c], ws[r-1][c-1], ws[r-2][c-2], ws[r-3][c-3]]) == 'XMAS':
                        total += 1
                # down left
                if go_down:
                    if ''.join([ws[r][c], ws[r+1][c-1], ws[r+2][c-2], ws[r+3][c-3]]) == 'XMAS':
                        total += 1

            # up/down directions
            if go_up:
                if ''.join([ws[r][c], ws[r-1][c], ws[r-2][c], ws[r-3][c]]) == 'XMAS':
                    total += 1
            if go_down:
                if ''.join([ws[r][c], ws[r+1][c], ws[r+2][c], ws[r+3][c]]) == 'XMAS':
                    total += 1
    
    print(total)

if __name__ == '__main__':
    main()
def main():
    with open('input.txt', 'r') as f:
        reports = f.read().strip().split('\n')
    
    safe_rep_amt = 0
    for r in reports:
        r_list = list(map(int, r.split()))

        for j in range(len(r_list) + 1):
            new_r_list = r_list.copy()
            if j < len(r_list):
                new_r_list.pop(j)
            is_inc = 1 if new_r_list[0] < new_r_list[1] else -1
            is_ok = True
            for i in range(len(new_r_list) - 1):
                if not 1 <= is_inc*(new_r_list[i+1] - new_r_list[i]) <= 3:
                    is_ok = False
                    break
            if is_ok:
                safe_rep_amt += 1
                break
    
    print(safe_rep_amt)
    
if __name__ == '__main__':
    main()
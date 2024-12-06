import itertools

def main():
    with open('input.txt', 'r') as f:
        (rules_raw, updates_raw) = f.read().strip().split('\n\n')
    
    rules = tuple([tuple(rule.split('|')) for rule in rules_raw.split()])
    updates = tuple([tuple(update.split(',')) for update in updates_raw.split()])

    final_sum = 0

    for u in updates:
        is_correct = True
        for i in range(len(u)):
            for j in range(i, len(u)):
                if (u[j], u[i]) in rules:
                    is_correct = False
                if not is_correct:
                    break
            if not is_correct:
                break
        if is_correct:
            continue
        
        r = []
        for pair in itertools.permutations(u, 2):
            if pair in rules:
                r.append(pair)
        
        pages_used = []
        for i in range((len(u)+1)//2):
            for page in set(u) - set(pages_used):
                if page not in (a[1] for a in r):
                    pages_used.append(page)
                    r = list(filter(lambda x: x[0] != page, r))
                    break

        final_sum += int(pages_used[-1])
    
    print(final_sum)

if __name__ == '__main__':
    main()
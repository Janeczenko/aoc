import os

with open(os.path.join(os.getcwd(),'05','input.txt')) as file:
    input = file.read().split('\n')
    num_nice = 0
    for i in input:
        if any(x in i for x in ['ab','cd','pq','xy']):
            continue
        three_vowels = sum(map(i.lower().count, "aeiou")) >= 3
        two_chars = False
        for n in range(len(i)-1):
            if i[n] == i[n+1]:
                two_chars = True
        if three_vowels and two_chars:
            num_nice += 1
    print(num_nice)
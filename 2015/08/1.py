import os
import re

def decodeVal(str):
    str = str[1:-1]
    (str,count1) = re.subn(r'\\x[0-9a-f]{2}','',str)
    (str,count2) = re.subn(r'\\.','',str)
    return len(str) + count1 + count2


with open('input.txt', 'r') as file:
    sum_all = 0
    sum_val = 0
    for line in file.read().split('\n'):
        line.replace('\n','')
        sum_all += len(line)
        sum_val += decodeVal(line)
    print(sum_all-sum_val)
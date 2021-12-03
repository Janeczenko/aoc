import os
import re

def encodeVal(str):
    print(str)
    str = re.sub(r'\\','\\\\\\\\',str)
    print(str)
    str = re.sub(r'"','\\"',str)
    print(str)
    str = '"'+str+'"'
    print(str)
    return len(str)


with open('input.txt', 'r') as file:
    sum_all = 0
    sum_val = 0
    for line in file.read().split('\n'):
        line.replace('\n','')
        sum_all += len(line)
        sum_val += encodeVal(line)
    print(sum_val-sum_all)
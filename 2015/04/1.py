import os
import hashlib

with open(os.path.join(os.getcwd(),'04','input.txt')) as file:
    code = file.read()
    i=0
    while True:
        code_tmp = code + str(i)
        hash = str(hashlib.md5(code_tmp.encode()).hexdigest())
        if hash[0:5] == '00000':
            break
        i+=1
    print(i)
def incrementStr():
    global input
    tmp = list(input)
    for i in range(len(tmp)-1,-1,-1):
        if tmp[i] != 'z':
            tmp[i] = chr(ord(tmp[i]) + 1)
            break
        else:
            tmp[i] = 'a'
    input = "".join(tmp)

def StrOfThree():
    global input
    for i in range(2, len(input)):
        if ord(input[i-2])+2 == ord(input[i-1])+1 == ord(input[i]):
            return True
    else:
        return False 

def notIOL():
    global input
    for i in range(len(input)):
        if input[i] in "iol":
            return False
    else:
        return True

def twoPairs():
    global input
    pairs = 0
    overlap = False
    for i in range(1,len(input)):
        if input[i-1] == input[i] and not overlap:
            pairs += 1
            overlap = True
        else:
            overlap = False
    if pairs >= 2:
        return True
    else:
        return False
        

with open("input.txt", "r") as f:
    input = f.read().strip()
    

incrementStr()

while not (StrOfThree() and notIOL() and twoPairs()):
    incrementStr()
else:
    print(input)
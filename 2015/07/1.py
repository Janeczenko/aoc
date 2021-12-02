import os

def func(input):
    global known_values
    while True:
        change = False
        for i in input:
            if 'NOT' in i:
                if i[1] in known_values or i[1].isnumeric():
                    known_values.setdefault(i[3],~(known_values[i[1]] if i[1] in known_values else int(i[1])))
                    input.pop(input.index(i))
                    change = True
            elif 'OR' in i:
                if (i[0] in known_values or i[0].isnumeric()) and (i[2] in known_values or i[2].isnumeric()):
                    known_values.setdefault(i[4],(known_values[i[0]] if i[0] in known_values else int(i[0]))|(known_values[i[2]] if i[2] in known_values else int(i[2])))
                    input.pop(input.index(i))
                    change = True
            elif 'AND' in i:
                if (i[0] in known_values or i[0].isnumeric()) and (i[2] in known_values or i[2].isnumeric()):
                    known_values.setdefault(i[4],(known_values[i[0]] if i[0] in known_values else int(i[0]))&(known_values[i[2]] if i[2] in known_values else int(i[2])))
                    input.pop(input.index(i))
                    change = True
            elif 'LSHIFT' in i:
                if i[0] in known_values or i[0].isnumeric():
                    known_values.setdefault(i[4],((known_values[i[0]] if i[0] in known_values else int(i[1]))<<int(i[2])))
                    input.pop(input.index(i))
                    change = True
            elif 'RSHIFT' in i:
                if i[0] in known_values or i[0].isnumeric():
                    known_values.setdefault(i[4],((known_values[i[0]] if i[0] in known_values else int(i[1]))>>int(i[2])))
                    input.pop(input.index(i))
                    change = True
            else:
                if i[0] in known_values or i[0].isnumeric():
                    known_values.setdefault(i[2],(known_values[i[0]] if i[0] in known_values else int(i[0])))
                    input.pop(input.index(i))
                    change = True
        if not change:
            return

with open(os.path.join(os.getcwd(),'07','input.txt')) as file:
    input = file.read().split('\n')
    input = [i.split(' ') for i in input]
    known_values = {}
    func(input.copy())
    print(known_values['a'])
    
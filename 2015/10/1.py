import itertools

def turn():
    global input
    new_input = ''
    for num,length in itertools.groupby(input):
        new_input += f'{len(list(length))}{num}'
    input = new_input


input = '1113122113'

for i in range(40):
    turn()
print(len(input))
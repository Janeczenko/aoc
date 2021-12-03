import itertools

def turn():
    global input
    new_input = ''
    for num,length in itertools.groupby(input):
        new_input += f'{len(list(length))}{num}'
    input = new_input


with open("input.txt", "r") as f:
    input = f.read().strip()

for i in range(40):
    turn()
print(len(input))
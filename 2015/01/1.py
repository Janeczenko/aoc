with open('input.txt', 'r') as file:
    floor = 0
    file_content = file.read()
    for i in range(len(file_content)):
        if file_content[i] == '(':
            floor+=1
        else:
            floor-=1
    else:
        print(floor)
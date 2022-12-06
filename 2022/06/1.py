def main():
    with open('input.txt', 'r') as f:
        characters = f.read().strip()
    index = 0
    while True:
        if len(set(characters[index:index+4])) == 4:
            break
        index += 1
    print(index + 4)


if __name__ == '__main__':
    main()
import itertools

def main():
    with open('input.txt', 'r') as f:
        disk_map = list(f.read().strip())

    disk = []
    file_id = 0
    is_file = True
    for length in disk_map:
        disk.extend([file_id if is_file else '.']*int(length))
        if is_file:
            file_id += 1
        is_file = not is_file
    
    block_amt = len(list(filter(lambda x: x != '.', disk)))

    last_full = len(disk) - 1
    while True:
        first_empty = disk.index('.')
        while disk[last_full] == '.':
            last_full -= 1
        if first_empty >= last_full:
            break
        (disk[first_empty], disk[last_full]) = (disk[last_full], disk[first_empty])
    
    checksum = sum(i*disk[i] for i in range(first_empty))
    print(checksum)



if __name__ == '__main__':
    main()
def main():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    current_path = []
    dir_sizes = {'/':0}

    for line_index in range(len(lines)):
        line_separated = lines[line_index].split(' ')
        if line_separated[0] == '$':
            # execute a command
            if line_separated[1] == 'cd':
                # change directory
                if line_separated[2] == '/':
                    current_path = ['/']
                elif line_separated[2] == '..':
                    current_path.pop()
                else:
                    current_path.append(line_separated[2])
                    dir_sizes.setdefault(line_separated[2], 0)
            else:
                # stay in a directory
                continue
        else:
            # add a file and its size
            if line_separated[0] != 'dir':
                for directory_name in current_path:
                    dir_sizes[directory_name] += int(line_separated[0])
    
    print(sum([(0 if x > 100000 else x) for x in dir_sizes.values()]))


if __name__ == '__main__':
    main()
import re


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
                    dir_sizes.setdefault('/'.join(current_path), 0)
            else:
                # stay in a directory
                continue
        else:
            # add a file and its size
            if line_separated[0] != 'dir':
                # FIXME: adapt for entire paths in `dir_sizes`. 
                for direcotry_path in ['/'.join(current_path[:x]) for x in range(1, len(current_path) + 1)]:
                    dir_sizes[direcotry_path] += int(line_separated[0])
                
    
    disk_space_needed = dir_sizes['/'] - 40000000
    print(min(list(filter(lambda x: x >= disk_space_needed, dir_sizes.values()))))


if __name__ == '__main__':
    main()
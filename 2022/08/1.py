def find_trees_coordinates(tree_list:list, second_coordinate:int, is_vertical:bool) -> set:
    visible_trees_coordinates_list = []
    max_height_start = -1
    max_height_end = -1
    for i in range(len(tree_list)):
        if max_height_start == max_height_end == 9:
            break
        if tree_list[i] > max_height_start:
            max_height_start = tree_list[i]
            visible_trees_coordinates_list.append((i, second_coordinate) if is_vertical else (second_coordinate, i))
        if tree_list[-i-1] > max_height_end:
            max_height_end = tree_list[-i-1]
            visible_trees_coordinates_list.append((len(tree_list)-i-1, second_coordinate) if is_vertical else (second_coordinate, len(tree_list)-i-1))
    return set(visible_trees_coordinates_list)


def main():
    with open('input.txt', 'r') as f:
        tree_matrix = [[int(y) for y in list(x)] for x in f.read().strip().split('\n')]
    visible_trees_coordinates_list = []
    for i, x in enumerate(tree_matrix):
        visible_trees_coordinates_list.extend(find_trees_coordinates(x, i, False))
    for j, y in enumerate([[tree_matrix[b][a] for b in range(len(tree_matrix))] for a in range(len(tree_matrix[0]))]):
        visible_trees_coordinates_list.extend(find_trees_coordinates(y, j, True))
    
    visible_trees_coordinates_list = set(visible_trees_coordinates_list)
    print(len(visible_trees_coordinates_list))


if __name__ == '__main__':
    main()
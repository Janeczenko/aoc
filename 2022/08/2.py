def find_scenic_score(tree_array:list[list[int]], coordinates:tuple[int]) -> tuple:
    current_tree = tree_array[coordinates[0]][coordinates[1]]
    if coordinates[0] == 0 or coordinates[0] == len(tree_array) - 1 or coordinates[1] == 0 or coordinates[1] == len(tree_array) - 1:
        return 0
    scenic_score = 1
    for direction in [-1, 1]:
        distance = 0
        while True:
            distance += 1
            if not 0 <= coordinates[1] + distance*direction < len(tree_array[0]):
                distance -= 1
                break
            if tree_array[coordinates[0]][coordinates[1] + distance*direction] >= current_tree:
                break
        scenic_score *= distance
        distance = 0
        while True:
            distance += 1
            if not 0 <= coordinates[0] + distance*direction < len(tree_array):
                distance -= 1
                break
            if tree_array[coordinates[0] + distance*direction][coordinates[1]] >= current_tree:
                break
        scenic_score *= distance
    return scenic_score


def main():
    with open('input.txt', 'r') as f:
        tree_matrix = [[int(y) for y in list(x)] for x in f.read().strip().split('\n')]
    max_scenic_score = 0
    for x in range(len(tree_matrix)):
        for y in range(len(tree_matrix[0])):
            max_scenic_score = max(max_scenic_score, find_scenic_score(tree_matrix, (x, y)))
    print(max_scenic_score)


if __name__ == '__main__':
    main()
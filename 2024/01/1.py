def main():
    with open('input.txt', 'r') as f:
        distances_list = f.read().strip().split('\n')
    distances_matrix = [entry.split() for entry in distances_list]
    dists_1 = sorted([int(i[0]) for i in distances_matrix])
    dists_2 = sorted([int(i[1]) for i in distances_matrix])
    dist_diff = [abs(dists_1[i] - dists_2[i]) for i in range(len(dists_1))]
    print(sum(dist_diff))

if __name__ == '__main__':
    main()
def main():
    with open('input.txt', 'r') as f:
        distances_list = f.read().strip().split('\n')
    distances_matrix = [entry.split() for entry in distances_list]
    dists_1 = [int(i[0]) for i in distances_matrix]
    dists_2 = [int(i[1]) for i in distances_matrix]
    
    sim_score = 0
    for i in range(len(dists_1)):
        for j in range(len(dists_2)):
            if dists_1[i] == dists_2[j]:
                sim_score += dists_1[i]
    
    print(sim_score)

if __name__ == '__main__':
    main()
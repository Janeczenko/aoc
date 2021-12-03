def filter_codes(data_f, filter_mode):
    for i in range(len(data_f[0])):
        if len(data_f) == 1:
            return data_f[0]
        count_0 = 0
        count_1 = 0
        for j in range(len(data_f)):
            if data_f[j][i] == "0":
                count_0 += 1
            else:
                count_1 += 1
        if count_0 > count_1:
            data_f = list(filter(lambda x: (x[i] == ("0" if filter_mode else "1")), data_f))
        elif count_0 < count_1:
            data_f = list(filter(lambda x: (x[i] == ("0" if not filter_mode else "1")), data_f))
        else:
            data_f = list(filter(lambda x: (x[i] == str(filter_mode)), data_f))
    return data_f[0]
        

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    
data_o = data.copy()
data_c = data.copy()

oxygen = filter_codes(data_o, 1)
co2 = filter_codes(data_c, 0)

print(int(oxygen, 2) * int(co2, 2))
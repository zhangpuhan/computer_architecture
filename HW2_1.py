branch_list = [0x1c6, 0x21f, 0x309, 0x21f, 0x309, 0x1c6, 0x309, 0x1c6, 0x21f]
true_take = [1, 0, 0, 0, 0, 1, 0, 1, 1]

BHT = [0, 0, 0, 0]
PHT = [[0, 0], [0, 0], [0, 0], [0, 0]]

for i in range(100):
    accuracy = 0
    prediction = []
    for j in range(len(branch_list)):
        PHT_index = int(bin(branch_list[j])[-2:], 2) % 4
        BHT_index = int("".join(map(str, PHT[PHT_index])), 2)
        prediction.append(BHT[BHT_index] // 2)
        if BHT[BHT_index] // 2 == true_take[j]:
            accuracy += 1

        if true_take[j] == 1:
            if BHT[BHT_index] != 3:
                BHT[BHT_index] += 1
        if true_take[j] == 0:
            if BHT[BHT_index] != 0:
                BHT[BHT_index] -= 1
        PHT[PHT_index].pop()
        PHT[PHT_index].insert(0, true_take[j])

    print("Round " + str(i) + ":")
    print("PHT:")
    print(PHT)
    print("BHT:")
    print(BHT)
    print("True take:")
    print(true_take)
    print("Prediction:")
    print(prediction)
    print("__________________")

    accuracy = accuracy / float(len(true_take))
    print(accuracy)

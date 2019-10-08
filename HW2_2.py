from collections import deque
branch_list = [0x1c6, 0x21f, 0x309, 0x21f, 0x309, 0x1c6, 0x309, 0x1c6, 0x21f]
true_take = [1, 0, 0, 0, 0, 1, 0, 1, 1]

BHT = [0 for _ in range(8)]

history_queue = deque(true_take[-3:])

for i in range(100):
    accuracy = 0
    prediction = []
    for j in range(len(true_take)):
        BHT_index = int("".join(map(str, list(history_queue))), 2)
        prediction.append(BHT[BHT_index] // 2)

        if BHT[BHT_index] // 2 == true_take[j]:
            accuracy += 1

        if true_take[j] == 1:
            if BHT[BHT_index] != 3:
                BHT[BHT_index] += 1
        if true_take[j] == 0:
            if BHT[BHT_index] != 0:
                BHT[BHT_index] -= 1

        history_queue.popleft()
        history_queue.append(true_take[j])

    print("Round " + str(i) + ":")
    print("BHT:")
    print(BHT)
    print("True take:")
    print(true_take)
    print("Prediction:")
    print(prediction)
    print("__________________")

    accuracy = accuracy / float(len(true_take))
    print(accuracy)

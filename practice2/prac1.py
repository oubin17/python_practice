for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) & (j != k) & (i != k):
                print(i, j, k)

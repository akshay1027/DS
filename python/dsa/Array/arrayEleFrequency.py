a = [1, 2, 1, 3, 2, 4]

count = 1
for i in range(len(a)):
    if a[i] > -1:
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                if a[j] > -1:
                    count += 1
                    a[j] = -1

        print(a[i], '-', count)
        count = 1

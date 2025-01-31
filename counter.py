a = [1, 3, 2, 5, 4]
result = [0]

for i in range(1, len(a)):
    counter = 0

    for j in a[:i]:
        if(a[i] < j):
            counter = counter - abs(a[i] - j)
        else:
            counter = counter + abs(a[i] - j)

result.append(counter)

inputs = sorted(map(int, input().split()))

n = len(inputs)

if len(inputs) % 2:
    print(inputs[len(inputs) // 2])

else:
    print(round(.5 + sum(inputs) / n))
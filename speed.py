import sys
import math

n = int(input())
k = 0
x = -1

for i in range(n):
    start,speed = [int(j) for j in input().split()]

    if speed == 0:
        continue
    t = start+100/speed

    if t==k:
        x=-1
    elif t>k:
        x = i
if k == 0:
    x=-1

    print(x, math.ceil(k))
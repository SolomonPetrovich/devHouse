import math

k, n = input().split()
k, n = map(int, (k, n))

coor = []

for i in range(k):
    coor.append(tuple(input().split()))

ans = 0
for i in range(k - 1):
    x = int(coor[i][0]) - int(coor[i + 1][0])
    y = int(coor[i][1]) - int(coor[i + 1][1])
    ans += math.sqrt(x*x + y*y)

print((ans * n)/50)

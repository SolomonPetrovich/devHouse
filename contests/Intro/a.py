m, n = input().split()
m, n = map(int, (m, n))

s = list(input())

for i in range(n):
    j = 0
    while j < (m - 1):
        if s[j] == 'B' and s[j + 1] == 'G':
            s[j] = 'G'
            s[j + 1] = 'B'
            step = 2
        else:
            step = 1
        j = j + step
print(*s, sep='')

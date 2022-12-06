n = int(input())
res = 0
for i in range(n):
    inp = input()
    if '++' in inp:
        res += 1
    elif '--' in inp:
        res -= 1

print(res)

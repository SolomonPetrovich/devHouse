n = int(input())

def do():
    s = input()
    t = input()
    p = input()
    sp = s + p

    sp_map = {}
    t_map = {}

    for i in sp:
        sp_map[i] = 0
    for i in t:
        t_map[i] = 0
    for i in sp:
        sp_map[i] += 1
    for i in t:
        t_map[i] += 1
    for i in t:
        if t_map[i] > sp_map[i]:
            return 'NO'

    return 'YES'

for i in range(n):
    print(do())

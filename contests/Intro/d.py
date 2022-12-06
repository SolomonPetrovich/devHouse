n = int(input())
p = list(map(int, list(input().split())))

off = 0
pres = 0
temp_pres = 0

for i in p:
    if off > 0:
        if i < 0:
            off -= 1
        elif i > 0:
            off += i
    else:
        if i > 0:
            off += i
        else:
            pres += 1

print(pres)

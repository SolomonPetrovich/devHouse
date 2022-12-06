s = list(sorted(set(input().split(','))))
s = list(map(int, s))

ans = []
temp = set()
for i in range(len(s) - 1):
    if s[i + 1] - s[i] == 1:
        temp.add(s[i])
        temp.add(s[i + 1])
    elif i == len(s)-1:
        print(temp)
        ans.append(temp)
    else:
        ans.append(temp)
        temp.clear()
        temp.add(s[i + 1])

print(ans)

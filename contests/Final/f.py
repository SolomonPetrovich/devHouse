n = int(input())

s = list(input())

ans = [s[0]]

for i in range(1, n):
    ans.append(s[i])
    
    if len(ans) > 1:
        if (ans[-1] == '0' and ans[-2] == '1') or (ans[-1] == '1' and ans[-2] == '0'):
            ans.pop()
            ans.pop()

print(len(ans))

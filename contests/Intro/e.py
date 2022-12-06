s = list(input())
cop = True
while True:
    for i, v in enumerate(s):
        if s[i] == s[i + 1]:
            s[i] = ''
            s[i + 1] = ''
        else:


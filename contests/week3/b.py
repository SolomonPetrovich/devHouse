def solve(s):
    a = [s[0]]
    for i in range(1, len(s)):
        a += s[i]
        if len(a) > 1:
            if (a[-2] == '{' and a[-1] == '}') or (a[-2] == '[' and a[-1] == ']') or (a[-2] == '(' and a[-1] == ')'):
                a.pop()
                a.pop()
    if len(a) > 0:
        print('NO')
    else:
        print('YES')

def main():
    n = int(input())
    for i in range(n):
        solve(input())


if __name__ == '__main__':
    main()

def solve():
    n = int(input())
    s = []
    
    for i in range(n):
        k, v = input().split()
        if k == '1':
            s.append(v)
        elif k == '2':
            s = s[:len(s) - int(v)]
        elif k == '3':
            s = print(s[int(v)])
        elif k == '4':
            
            pass


def main():
    solve()


if __name__ == '__main__':
    main()

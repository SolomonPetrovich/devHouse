def solve():
    
    n = int(input())

    d = {'polycarp': 1}

    for i in range(n):
        s = input().split()
        if s[0].lower() not in d.keys():
            d[s[0].lower()] = d[s[-1].lower()] + 1
    
    print(max(d.values()))


def main():
    solve()


if __name__ == '__main__':
    main()

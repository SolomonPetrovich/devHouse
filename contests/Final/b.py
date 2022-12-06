def solve():
    n = int(input())

    stones = list(map(int, input().split()))
    sorted_stones = sorted(stones) 
    
    m = int(input())
    
    s = [stones[0]]
    sorted_s = [sorted_stones[0]]
    
    for i in range(1, len(stones)):
        s.append(s[i-1] + stones[i])

    for i in range(1, len(sorted_stones)):
        sorted_s.append(sorted_s[i-1] + sorted_stones[i])
    
    for i in range(m):
        typ, l, r = input().split()
        typ, l, r = map(int, (typ, l, r))
        if typ == 1:
            if l == 1:
                print(s[r-1])
            else:
                print(s[r-1] - s[l-2])
        elif typ == 2:
            if l == 1:
                print(sorted_s[r-1])
            else:
                print(sorted_s[r-1] - sorted_s[l-2])

def main():
    solve()


if __name__ == '__main__':
    main()

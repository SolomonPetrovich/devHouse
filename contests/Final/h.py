m, n = map(int, input().split())
count = 0

if m > n:
    print(int((m - n)/n))
else:
    while True:
        if n == m:
            break

    print(count)
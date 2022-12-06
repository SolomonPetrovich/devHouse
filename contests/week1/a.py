n = input().strip()
arr = list(input().split())

arr = list(map(int, arr))

sorted_arr = sorted(arr)

if sum(sorted_arr[:len(sorted_arr)//2]) == sum(sorted_arr[len(sorted_arr)//2:]):
    print("-1")
else:
    print(*sorted_arr)

def solve(nums: list):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            nums[i] = -1
    
    nums.sort()
    nums = [i for i in nums if i > -1]
    
    print(nums)
    return len(nums)


def main():
    n = [0,0,1,1,1,2,2,3,3,4]
    print(solve(n))


if __name__=='__main__':
    main()

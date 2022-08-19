def check(n):
    if n < 5:
        return n
    else:
        return 6


nums = [4,7,2,5,1,6,3,8]
print(sorted(nums, key=check))



def sum123(nums):
    result = 0
    for n in nums:
        result += n
    return result


def sum124(*nums):
    result = 0
    for n in nums:
        result += n
    return result

print(sum123([10,20,30]))
print(sum124(10,20,30))
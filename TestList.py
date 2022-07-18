from ast import Num
from itertools import count


nums = [10, 20, 30, 40, 50]
print(nums)
print(type(nums))

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

nums.append(60) # add at last
print(nums)

nums.insert(len(nums), 70) # add at last(position len(nums))
print(nums)

nums.remove(10) # remove 10 in nums
print(nums)

del nums[0] # delete first in nums
print(nums)

nums.insert(0, -10) # add at position 0
print(nums)

print(len(nums))

'''
from sys import argv
print(type(argv))
print(argv)
'''
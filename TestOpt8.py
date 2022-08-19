nums = [10,20,30,40,50,60]

print(nums[0:2])
print(nums[2:4])
print(nums[2:-2])

nums2 = (10,20,30,40,50,60)
print(nums2[0:2])

'''
nums3 = {10,20,30,40,50}
print(nums3[0:2])
'''

nums[2:4] = [200,350,400]
print(nums)

del nums[2:5] # delete 2~4
print(nums)
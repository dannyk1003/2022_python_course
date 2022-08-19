nums = [10,20,30]
nums2 = []
for num in nums:
    print(num**2)
    nums2.append(num**2)
print(nums2)

###
print([num**2 for num in nums])
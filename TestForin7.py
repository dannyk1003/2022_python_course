nums = [[10,20,30],[40,50,60],[70,80,90]]

nums3 = []

for i in nums:
    nums2 = []
    for j in i:
        #print(j + 2)
        nums2.append(j + 2)
    nums3.append(nums2)

print(nums2)
print(nums3)

print([j + 2 for i in nums for j in i ])
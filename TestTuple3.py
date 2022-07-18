nums1 = (10, 20, 30)
nums2 = list(nums1)
nums2.append(40)
print(nums2)
print(type(nums2))

nums3 = tuple(nums2)
print(type(nums3))

nums4 = set(nums3)
print(type(nums4))
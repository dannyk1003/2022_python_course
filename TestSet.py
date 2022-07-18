nums = {10,20,30}
print(nums)
print(type(nums))

nums.add(40) # add one in set
print(nums)

nums.update({50, 60}) # add more in set
print(nums)

nums.remove(20) # remove one
print(nums)


nums.difference_update({50, 60}) # remove more
print(nums)

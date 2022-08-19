text = ['aBCD', 'Bcd', 'Cd']
nums = [3, 1, 2, 5, 4]
print(sorted(nums))
print(sorted(nums, reverse=True))

print(sorted(text))
print(sorted(text, key = len))
print(sorted(text, key = str.upper))
print(str.upper('abc'))
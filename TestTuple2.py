x = 10
y = 20

x, y = y, x
print('x=', x)
print('y=', y)

nums1 = (10, 20, 30)
a, b, c = nums1
print(type(nums1))
print(a)
print(b)
print(c)

nums2 = [40, 50, 60]
d, e, f = nums2
print(type(nums2))
print(d)
print(e)
print(f)

nums3 = (10,20,30,40,50)
i, *j, k = nums3
print('i = ', i)
print('j = ', j)
print('k = ', k)
print(type(j))
print(type(nums3))
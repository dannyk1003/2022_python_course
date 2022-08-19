nums1 = [10,20,30,40,50] # list
nums2 = {10,20,30,40,50} # set
nums3 = (10,20,30,40,50) # tuple

#nums = input('enter data nums : ')
#print( nums , 'data type : ' , )




print(nums1[0])
print(nums3[1])
print(list(nums2)[2])


data1 = (('a',1),('b',2))
data2 = [['a',1],['b',2]]
#data3 = {{'a',1},{'b',2}}

print(type(data1),type(data2))
print(data1,data2)
print(dict(data1),dict(data2))
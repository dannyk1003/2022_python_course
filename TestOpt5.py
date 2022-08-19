print(3&6) # and &
print(3&7)

'''
3   0011
&6  0110
2   0010
'''

print(3|6) # or |
print(3|7)

'''
3   0011
|6  0110
7   0111
'''

print('3 : ' , bin(3))
print('6 : ' , bin(6))
print('7 : ' , bin(7))

print(9&6)
print(9|6)

'''
3   0011
^7  0111
4   0100
'''
print(3^7)
print(6^9)
print(int(0b01111111))
print(int(~0b10000000))
print(bin(-128))
print(3 , ~3) # 012(3) / -1-2-3(-4)


print(15>>2) # 1111 >> 2 = 0011
print(15>>2<<2) ## 1111 >> 2 = 0011; 0011 << 2 = 1100
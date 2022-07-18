print('Str: %s, Int: %d, Float: %f' %('Hello', 10, 3.14))
print('Str: {}, Int: {}, Float: {}'.format('Hello', 10, 3.14)) # use {} replace %
print('Str: {1}, Int: {2}, Float: {0}'.format('Hello', 10, 3.14))

print('Str: {:s}, Int: {:d}, Float: {:f}'.format('Hello', 10, 3.14))
print('Str: {0:s}, Int: {1:d}, Float: {2:f}'.format('Hello', 10, 3.14))
#print('Str: {1:s}, Int: {2:d}, Float: {0:f}'.format('Hello', 10, 3.14)) # wrong data type

print('Str: {0:<7s}, Int: {1:d}, Float: {2:f}'.format('Hello', 10, 3.14)) # if < than space on right side 
print('Str: {0:>7s}, Int: {1:d}, Float: {2:f}'.format('Hello', 10, 3.14)) # if > than space on left side 
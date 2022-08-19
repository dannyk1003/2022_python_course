def sum124(nums):
    r = 0
    for i in nums:
        r += i
    print(r)

sum124([10,20,30])


def gcd(m, n):
    if n == 0:
        return m
    else:
        print(m, n)
        return gcd(n, m%n)
        
print(gcd(105,252))

def gcdx(m,n):
    while n != 0:
        n, m = m % n, n
    print(m) 

gcdx(105,252)
gcdx(6,9)
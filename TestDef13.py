def test():
    global x
    x = 20
    print(x)
    print(locals())

x = 10
test()
print(x)
print(locals())
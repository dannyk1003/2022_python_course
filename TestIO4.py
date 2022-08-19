with open('data1.txt', 'r') as fr:
    #print(list(fr))
    print('1: ', fr.tell())
    print(fr.readline())
    print('2: ', fr.tell())
    print(fr.readline())
    print('3: ', fr.tell())
    fr.seek(0)
    print(fr.read())
    fr.seek(0)
    #print(list(fr))
    for line in fr:
        print(line, end='')
        #print(line)
    fr.seek(0)
    with open('data2.txt', 'w') as fw:
        print(fr.read())
        fr.seek(0)
        fw.write(fr.read())


'''
with open('data1.txt', 'r') as fr:
    with open('data2.txt', 'w') as fw:
        print(fr.read())
        #fr.seek(0)
        fw.write(fr.read())
    #print(fr.read())
'''

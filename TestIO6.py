with open('data3.txt') as fr:
    with open('data4.txt', 'w') as fw:
        print(fr.read())
        fr.seek(0)
        fw.write(fr.read())

with open('data3.txt', 'rb') as fr:
    print(fr.read())


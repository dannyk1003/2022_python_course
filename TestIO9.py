with open('cat.jpg', 'rb') as fr:
    with open('cat2.jpg', 'wb') as fw:
        fw.write(fr.read())
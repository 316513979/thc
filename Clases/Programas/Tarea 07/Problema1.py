def listas(a, b):
    i=0
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                i=i+1
            else:
                print 'Las listas son diferentes'

    else:
        print 'Las listas son diferentes'
    if i == len(a):
        print 'Las listas son iguales'

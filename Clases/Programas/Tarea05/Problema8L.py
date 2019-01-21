def paresimpares (a, b):
    x=a
    i=0
    j=0
    P=[]
    I=[]
    while a<=x and x<=b:
        if (x/2)*2 == x:
            i=i+1
            P.append(x)
        else:
            j=j+1
            I.append(x)
        x=x+1
    print  ('Entre %d y %d hay %d enteros pares:' % (a, b, i))
    print P
    print (' y %d enteros impares:' % (j))
    return I

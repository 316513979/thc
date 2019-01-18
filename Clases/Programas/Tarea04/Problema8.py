def paresimpares (a, b):
    x=a
    i=0
    j=0
    while a<=x and x<=b:
        if (x/2)*2 == x:
            i=i+1
        else:
            j=j+1
        x=x+1
    return  ('Entre %d y %d hay %d enteros pares y %d enteros impares' % (a, b, i, j))

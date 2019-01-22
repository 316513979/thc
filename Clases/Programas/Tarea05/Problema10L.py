# -*- coding: utf-8 -*-
def mult3(a, b):
    L=[]
    if a<=b:
        j=a
        while a<=j and j<=b:
            r=j%3
            if r == 0:
                L.append(j)
            j=j+1
        print 'Entre %d y %d los multiplos de 3 son: ' % (a, b)
    else:
        j=b
        while b<=j and j<=a:
            r=j%3
            if r == 0:
                L.append(j)
            j=j+1
        print 'Entre %d y %d los multiplos de 3 son: ' % (b, a)
    return L

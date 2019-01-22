# -*- coding: utf-8 -*-
def mult3(a, b):
    i=0
    if a<=b:
        j=a
        while a<=j and j<=b:
            r=j%3
            if r == 0:
                i=i+1
            j=j+1
    else:
        j=b
        while b<=j and j<=a:
            r=j%3
            if r == 0:
                i=i+1
            j=j+1
    return ('Entre %d y %d hay %d multiplos de 3.' % (a, b, i))

# -*- coding: utf-8 -*-

def mult3(a, b):
    x=a
    i=0
    while a<=x and x<=b:
        d=x%3
        if d == 0:
            i=i+1
        x=x+1
    return 'Entre %d y %d hay %d múltiplos de 3' % (a, b, i)
    

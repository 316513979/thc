# -*- coding: utf-8 -*-
def mult3(a, b):
    x=a
    L=[]

    while a<=x and x<=b:
        d=x%3
        if d == 0:
            L.append(x)
        x=x+1
    print 'Los múltiplos de 3 desde %d hasta %d son: ' % (a, b)
    return L

# -*- coding: utf-8 -*-

def resolver(L, e):
    n = len(L[0])
    m=len(L)
    x = e[0]
    y = e[1]
    if y == n-1 or x==m-1: # Para ver si ya terminó al pasarse al cuadro de abajo.
        return e[0]+1, e[1]+1
    else:
        if L[x][y+1]==False:
            e = [x, y+1]
            return resolver (L, e)
        #else:
        #    if L[x+1][y]==False:
        elif L[x+1][y] == False:
            e=[x+1, y]
            return resolver (L,e)
        else:
            print 'ya no puede avanzar al frente.'
                
L=[[True, True, True, True],
   [False, False, False, True],
   [True, True, False, True]]   
type(L)
e=[1,0]
r=resolver(L, e)
import numpy as np
print(np.matrix(L))

# -*- coding: utf-8 -*-
# No pude completar el programa.

def resolver(L, e):
    n = len(L[0])
    m=len(L)
    x = e[0]
    y = e[1]
    if y == n-1 or x==m-1 or x-2<0:    # No se me ocurrió una forma en que el programa identifique la salida cuando está en la primer fila.
        return e[0]+1, e[1]+1
    else:
        if L[x][y+1]==False:
            e = [x, y+1]
            print e
            return resolver (L, e)
        elif L[x+1][y] == False:
            e=[x+1, y]
            print e
            return resolver (L,e)
        elif L[x-1][y] == False:       # Este es un desplazamiento hacia arriba. 
            e=[x-1, y]
            print e
            return resolver (L, e)
        else:
            print 'ya no puede avanzar al frente.'

L=[[True, True, False, True],
   [False, False, False, True],
   [True, True, True, True]]   
type(L)
e=[1,0]
r=resolver(L, e)

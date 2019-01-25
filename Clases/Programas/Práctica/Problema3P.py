# -*- coding: utf-8 -*-
def sumacubo(n):
    i=1
    s=0
    while i<=n:
        j=i**3      # El ciclo toma los valores de los enteros previos al entero n.
        s=s+j       # a cada uno lo eleva al cubo y el resultado se guarda en la variable j.
        i=i+1       # En esta variable se va guardando la suma de los enteros elevados al cubo.
    print 'La suma del cubo de los primeros %d enteros calculada con el programa es: ' % (n)
    print s
    f = ((n*(n+1))/2.0)**2
    print 'La suma del cubo de los primeros %d enteros calculada con la fórmula es: ' % (f)
    print f
    d= f-s
    print 'La diferencia entre ambos resultados es: '
    print d

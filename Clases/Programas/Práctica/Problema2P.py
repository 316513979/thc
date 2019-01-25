# -*- coding: utf-8 -*-
def sumacuadrada(n):
    i=1
    s=0
    while i<=n:              # El ciclo toma los valores de los enteros previos al entero n.
        j=i**2               # a cada uno lo eleva al cuadrado y el resultado se guarda en la variable j.  
        s=s+j                # En esta variable se va guardando la suma de los enteros elevados al cuadrado. 
        i=i+1
    print 'La suma del cuadrado de los primeros %d enteros calculada con el programa es: ' % (n)
    print s
    f = (n*(n+1)*((2.0*n)+1))/6.0
    print 'La suma del cuadrado de los primeros %d enteros calculada con la fórmula es: ' % (f)
    print f
    d= f-s
    print 'La diferencia entre ambos resultados es: '
    print d

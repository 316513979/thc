#!/usr/bin/python2.7
# -*- coding: utf-8 -*
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa despliega todas las multiplicaciones de enteros cuyo 
# producto es un entero dado.

import Problema9L

a=input ('Introduce un número para conocer sus divisores: ')
L=Problema9L.divisibilidad(a)
print 'Los divisores de %d son: ' % (a)
for l in L:
        print '%d x %d = %d' % (l, (a/l), a)

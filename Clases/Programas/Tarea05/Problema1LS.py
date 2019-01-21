#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es calcular el máximo común divisor de dos números
# enteros cualesquiera y desplegar en una lista los residuos que se van obteniendo
# al calcular el M.C.D a través del algoritmo de Euclides.

import Problema1L
print '''Dados dos enteros, a y b, el algoritmo de Euclides consiste en la
fórmula a=(bq)+r donde q y r son enteros y r es llamado residuo. Si en esta expresión
r=0 entonces el M.C.D de a y b es q. De cualquier otra forma se utiliza el valor
de r para generar la expresión b=r(q1)+r1 donde q1 y r1 son enteros. A esta expresión
se le aplican los mismos criterios que a la anterior por lo que el proceso sigue
hasta que el residuo rn es 0.'''
a=input ('Introduce un entero: ')
b=input ('Introduce otro entero: ')
print 'Los residuos obtenidos con el algoritmo de Euclides para hallar el M.C.D son: '
print Problema1L.mcd(a, b)

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es utilizar las fórmulas de tiro parabólico
# para calcular a partir de una determinada velocidad inicial (m/s) la altura (m) de la
# pelota con respecto a su altura inicial en 11 instantes distintos de tiempo (s).
# La diferencia entre los instantes de tiempo es constante y las alturas se
# se despliegan como valores en una lista. 

import Problema2L
g=-9.81

v0=input ('Introduce la velocidad inicial de la pelota (m/s): ')
tf= (-2.0)*v0*(1.0/g)
print Problema2L.posicion(v0)
print 'Estas son las alturas de la pelota (m) desde t=0 s hasta t=%.3f s' % (tf)

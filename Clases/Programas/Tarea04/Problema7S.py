#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa calcula el promedio de 10 valores cualesquiera así como el
# mayor y menor de ellos. 

import Problema7
a, b, c, d, e, f, g, h, i, j= input ("Introduce 10 valores: ")
print ("Promedio: %.3f" % (Problema7.promedio(a, b, c, d, e, f, g, h, i, j)))
print ("Mayor: %.3f" % (Problema7L.mayor(a, b, c, d, e, f, g, h, i, j)))
print ("Menor: %.3f" % (Problema7L.menor(a, b, c, d, e, f, g, h, i, j)))

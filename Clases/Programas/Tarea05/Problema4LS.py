#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa despliega una lista que contiene los primeros n términos de la sucesión
# de Fibonnaci. 

import Problema4L

n=input ('Número de término de la sucesión de Fibonacci hasta el quieres conocer: ')
print 'Los términos de la sucesión de Fibonacci hasta el %d término son:' % (n)
print Problema4L.fib (n)

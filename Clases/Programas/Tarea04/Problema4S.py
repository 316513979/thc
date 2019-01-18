#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa permite calcular el enésimo término de la sucesión de Fibonacci.

import Problema4

n=input ('Introduce el número de término de la sucesión de Fibonacci que quieres conocer: ')
print 'El término número %d de la sucesión de Fibonacci es %d' % (n, Problema4.fib(n))

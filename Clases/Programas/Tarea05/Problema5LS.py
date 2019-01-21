#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa despliega una lista con los totales que se van generando al sumar
# los números naturales desde el 0 hasta el natural "n".

import Problema5L
n=input ("Introduce un número natural: ")
print ("Los totales obtenidos al sumar los números naturales desde el 0 hasta el %d son: " % (n))
print Problema5L.sumanaturales(n)     

       



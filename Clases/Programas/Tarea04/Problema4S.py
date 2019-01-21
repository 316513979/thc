#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa permite calcular el enésimo término de la sucesión de Fibonacci.
# Para poder construirlo tuve que basarme en un ejercicio similar que encontre
# en el link https://www.w3resource.com/python-exercises/python-conditional-exercise-9.php
# porque no se me ocurrían las operaciones a efectuar entre las variables
# para encontrar los términos. Gracias al ejercicio de internet me di cuenta
# de que como había que organizar las variables para que se generaran los términos
# de la sucesión.

import Problema4

n=input ('Introduce el número de término de la sucesión de Fibonacci que quieres conocer: ')
print 'El término número %d de la sucesión de Fibonacci es %d' % (n, Problema4.fib(n))

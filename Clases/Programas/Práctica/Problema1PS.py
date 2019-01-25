#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Este programa convierte una medida de temperatura en la escala Fahrenheit
# a su equivalencia en la escala Celsius utilizando 2 fórmulas diferentes:
# una exacta y una aproximación. También calcula la diferencia entre el resultado
# de ambas fórmulas. Al final despliega todos los resultados en una tabla.

import Problema1P

f= input ('''Introduce una temperatura en grados Fahrenheit para transformarla a
          su equivalente en grados Centígrados: ''')
print Problema1P.convertir(f)

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es utilizar las fórmulas de tiro parabólico
# para calcular a partir de la velocidad inicial y la altura de un proyectil
# el instante en el que se encuentra.

import Problema2

v0=input ('Introduce la velocidad inicial de la pelota (m/s): ')
y=input ('Introduce la altura en (m): ')
print Problema2.tiempo(v0, y)


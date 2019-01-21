#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es calcular el máximo común divisor de dos enteros
# cualesquiera.

import Problema1

x, y= input ('Escribe dos números enteros: ')
z= Problema1.mcd(x, y)
print ('El máximo común divisor de %d y %d es %d.' % (x, y, z))

       

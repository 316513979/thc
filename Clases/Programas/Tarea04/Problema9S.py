#!/usr/bin/python2.7
# -*- coding: utf-8 -*
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es convertir el valor de una determinada cantidad
# de pesos a dólares o viceversa. 

import Problema9

x=input ('Convertir: ')

if x == 'dólares a pesos':
    d=input ('Introduce la cantidad de dólares: ')
    t=input ('Introduce el tipo de cambio: ')
    print Problema9.dolarpeso(d, t)
else:
    a=input ('Introduce la cantidad de pesos: ')
    k=input ('Introduce el tipo de cambio: ')
    print Problema9.pesodolar(a, k)

    

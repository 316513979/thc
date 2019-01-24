#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa determina si dos listas dadas son iguales o diferentes.

import Problema1

print '''Las listas son conjuntos de números o caractéres delimitados por
corchetes ([]). Asegúrate de separar los elementos con comas y de escribir
los caractéres entre comillas.'''
a=input ('Introduce una lista: ')
b=input ('Introduce otra lista: ')
print Problema1.listas(a, b)

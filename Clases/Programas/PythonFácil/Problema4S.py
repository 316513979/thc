#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es enlistar todos los múltiplos de un entero x. 

import Problema4

x=input ('Introduce un entero para enlistar todos sus múltiplos: ')
L=Problema4.lista_infinita(x)

for n in L:
    print n
    

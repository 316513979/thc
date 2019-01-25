#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import Problema7AP

print '''Esta es la función dada por 0, si x < -e,
H= 1/2+x/(2e)+(1/(2e))(sen((3.14159x)/e) si -e<=x<=e y 1 si e<x'''

x=input ('Introduce un número para evaluarlo en la función: ')
print Problema7AP.H_eps(x)


     

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionale
# Este problema es muy parecido al problema 6: ambos arrojan el promedio de 10 números. La diferencia
# está en que en este se utilizan listas y el ciclo for
# para calcularlo. Esto hace que también funcione como media ponderada de modo
# que a cada valor se le podría dar un "peso" distinto. Por ello
# es de utilidad para la labor docente. 

import Problema6L

a, b, c, d, e, f, g, h, i, j= input ("Introduce 10 valores: ")
print (Problema6L.promedio(a, b, c, d, e, f, g, h, i, j))

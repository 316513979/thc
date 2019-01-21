#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# El objetivo de este programa es desplegar los días de asueto oficiales
# correspondientes a cada mes del 2019. Las listas lo simplificaron porque
# cada día de asueto se reemplazó por una variable. Esto hace el programa
# más corto y ordenado. Además no hubo que reescribir la cadena 'no hay días
# de asueto oficiales' en los meses correspondientes. 

import Problema10L

x=input ('Introduce un mes para conocer los días de asueto oficiales correspondientes: ')
print Problema10L.diasasueto (x)

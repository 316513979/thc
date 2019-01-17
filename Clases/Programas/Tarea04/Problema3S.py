#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import Problema3

a=input ('Convertir de grados ')
b=input ('a grados ')

if a == 'centígrados' and b == 'fahrenheit':
    x= input ('Introduce la temperatura en grados centígrados: ')
    print Problema3.CentigradosFahrenheit (x)
else:
    if a == 'fahrenheit' and b == 'centígrados':
        x= input ('Introduce la temperatura en grados fahrenheit: ')
        print Problema3.FahrenheitCentigrados (x)
    else:
        print ('Error')
        
    

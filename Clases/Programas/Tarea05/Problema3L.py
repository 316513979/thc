# -*- coding: utf-8 -*-
import TareaFuncionRangeFloat

def CentigradosFahrenheit (ti, tf):
    d= (tf-ti)/10.0
    L= TareaFuncionRangeFloat.rangefloat(ti, tf, d)
    print '  ºC    ºF'
    for l in L:
        f= ((9*l)/5.0) + 32
        print ('%5.2f %5.2f' % (l, f))

def FahrenheitCentigrados (ti, tf):
    d= (tf-ti)/10.0
    J= TareaFuncionRangeFloat.rangefloat(ti, tf, d)
    print '  ºF    ºC'
    for j in J:
        y= (5*(j-32))/9
        print ('%5.2f %5.2f' % (j, y))
    


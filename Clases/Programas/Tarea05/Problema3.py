# -*- coding: utf-8 -*-
import TareaFuncionRangeFloat

def CentigradosFahrenheit (ti, tf):
    d= (tf-ti)/10.0
    L= TareaFuncionRangeFloat(ti, tf, d)
    print '     ºC    ºF'
    for l in L:
        f= ((9*l)/5.0) + 32
        return ('%5.2f %5.2f' % (l, f))
    

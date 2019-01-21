# -*- coding: utf-8 -*-
import TareaFuncionRangeFloat

def posicion(v0):
    g=-9.81
    tf= (-2.0)*v0*(1.0/g)
    d= (tf/10.0)
    t=0
    A= []
    if tf == 0:
        A.append(0)
    else:
        while t<=tf:
            y = v0*t + (1.0/2)*g*(t**2)
            A.append(y)
            t=t+d
    return A



        

  

    


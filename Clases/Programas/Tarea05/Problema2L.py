# -*- coding: utf-8 -*-
# El problema 2L es diferente al problema 2: ahora a partir de la velocidad inicial
# se calcula la altura de la pelota con respecto al punto de lanzamiento en distintos
# instantes de tiempo. Esta modificación la hice porque considero que es más
# interesante calcular la altura de la pelota a lo largo de un intervalo de tiempo
# ya que esta información da una mejor idea de su trayectoria. Por esta misma razón me pareció
# de mayor utilidad agregar esta información a una lista pues después se puede
# utilizar para trazar una gráfica.

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



        

  

    


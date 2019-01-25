# -*- coding: utf-8 -*-
def factorial(n):
    if n==0:
        return 1
    else:
        return n*(factorial(n-1))    # Aquí se logra la recursión porque se van
                                    # acumulando los factores. En ese sentido esta parte funciona como una variable. 
    


# -*- coding: utf-8 -*-
# Ejercicio: programa que hicimos nosotros

def ulam(x):
    i=0
    print(x)
    while x>1:
        p=x/2
        if 2*p == x :
            x=x/2
            i=i+1
            print(x)
        else :
            i=i+1
            x=3*x+1
            print(x)
    return('La operación se ejecutó %d veces' % (i))


print ulam(6)
print ulam(17)



# Programa del profesor:
'''
def Ulam (x):
    #if (x/2)*2-x == 0: la operación módulo %
    #a partir de esta operación determina la paridad de un número.
    if x%2 == 0:
        return x/2
    else:
        return 3*x+1

def suc(x):
    i=0
    #while x>1:
    while x!=1:
        x=ulam(x)
        i=i+1
    return i

print suc(7)
print suc(26)
print suc(52)
print suc(1024)
print suc(72)
print suc(1524927)
print suc(2)

#Es preferible hacer un programa por partes.'''

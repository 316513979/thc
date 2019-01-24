# -*- coding: utf-8 -*-

# Sumas de la función f(x)=2-(x^2)
print '''Este programa arroja el valor de las áreas interiores, exteriores y
de los trapecios correspondientes a la función f(x)=2-(x^2) que están dentro del
intervalo [-1, 1].'''

L=[-1, -0.5, 0, 0.5]
Si=0
for i in L:
    j=i+0.5
    hi = 2 - (i**2)
    hj = 2 - (j**2)
    if hi<hj:
        A = hi*0.5
    else:
        A = hj*0.5
    Si = Si + A
print 'Suma de las áreas interiores: %.3f' % (Si)

L=[-1, -0.5, 0, 0.5]
Ss=0
for i in L:
    j=i+0.5
    hi = 2 - (i**2)
    hj = 2 - (j**2)
    if hi<hj:
        A = hj*0.5
    else:
        A = hi*0.5
    Ss = Ss + A
print 'Suma de las áreas exteriores: %.3f' % (Ss)

L=[-1, -0.5, 0, 0.5]
S= 0
for i in L:
    j=i+0.5
    hi = 2 - (i**2)
    hj = 2 - (j**2)
    if hi<hj:
        R = hi*0.5
        a = hj-hi
        T = (0.5*a)/(2.0)
    else:
        R = hj*0.5
        a = hi-hj
        T = (0.5*a)/(2.0)
    S= S+R+T
print 'Suma de los trapecios: %.3f' % (S)

print '________________________________________________________________________'


# Sumas de la función h(x)=-6(x^3)+5(x^2)+2x+12
print '''Este programa arroja el valor de las áreas interiores, exteriores y
de los trapecios correspondientes a la función h(x)=-6(x^3)+5(x^2)+2x+12 que
están dentro del intervalo [-1, 1].'''

L=[-1, -0.5, 0, 0.5]
Si=0
for i in L:
    j=i+0.5
    hi = (-6.0*(i**3))+(5.0*(i**2))+(2.0*i)+12
    hj = (-6.0*(j**3))+(5.0*(j**2))+(2.0*j)+12
    if hi<hj:
        A = hi*0.5
    else:
        A = hj*0.5
    Si = Si + A
print 'Suma de las áreas interiores: %.3f' % (Si)

L=[-1, -0.5, 0, 0.5]
Ss=0
for i in L:
    j=i+0.5
    hi = (-6.0*(i**3))+(5.0*(i**2))+(2.0*i)+12
    hj = (-6.0*(j**3))+(5.0*(j**2))+(2.0*j)+12
    if hi<hj:
        A = hj*0.5
    else:
        A = hi*0.5
    Ss = Ss + A
print 'Suma de las áreas exteriores: %.3f' % (Ss)

L=[-1, -0.5, 0, 0.5]
S= 0
for i in L:
    j=i+0.5
    hi = (-6.0*(i**3))+(5.0*(i**2))+(2.0*i)+12
    hj = (-6.0*(j**3))+(5.0*(j**2))+(2.0*j)+12
    if hi<hj:
        R = hi*0.5
        a = hj-hi
        T = (0.5*a)/(2.0)
    else:
        R = hj*0.5
        a = hi-hj
        T = (0.5*a)/(2.0)
    S= S+R+T
print 'Suma de los trapecios: %.3f' % (S)

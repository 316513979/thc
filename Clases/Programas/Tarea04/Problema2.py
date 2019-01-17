# -*- coding: utf-8 -*-
import math
g = 9.81
def tiempo(v0, y):
    t1 = (v0 + math.sqrt(((v0)**2)-2.0*g*y))/g
    t2 = (v0 - math.sqrt(((v0)**2)-2.0*g*y))/g
    if t1 == t2:
        return ('La pelota alcanzó esta altura a los %.3f segundos' % (t1))
    else:
        return ('La pelota alcanzó esta altura a los %.3f segundos y a los %.3f segundos' % (t1, t2))

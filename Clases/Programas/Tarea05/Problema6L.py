def promedio(a, b, c, d, e, f, g, h, i, j):
    L=[a, b, c, d, e, f, g, h, i, j]
    s=0
    for i in L:
        i=(0.1)*i
        s=s+i
    return ('El promedio es: %.2f' % (s))

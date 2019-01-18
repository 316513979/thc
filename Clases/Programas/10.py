# -*- coding: utf-8 -*-
S='____________________'
C=-20
iC=5
print '    C    F'
while C <= 40:
    F = (9.0/5)*C +32
    print C, F
    #C = C + iC
    C += iC

print S
gradosC = [-20, -15, -10, -5, 0, 5, 10, 15, 20]
print '    C    F'
for grado in gradosC:
    F = (9.0/5)*grado + 32
    print '%5d %5.1f' % (grado, F)
    
print S
indice = 0
print '    C     F'
while indice < len(gradosC):
    C=gradosC[indice]
    F = (9.0/5)*C + 32
    # print C, F
    print '%5d %5.1f' % (C, F)
    indice += 1
print S
#Los dos programas anteriores son equivalentes, ambos recorren una lista

gradosC=[]
for C in range (-20, 45, 5):
    gradosC.append(C)
print grados C
# Agrega a la lista todos los números desde el -20 hasta antes del 45,
# incrementando cada vez 5 unidades.

print S
gradosC=[]
for i in range(0, 21):
    C= -20+i*2.5
    gradosC.append(C)
print gradosC

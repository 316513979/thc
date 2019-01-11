# -*- coding: utf-8 -*-
i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
# Los números se colocan entre comillas para mostrar el campo de escritura
print '"%d"' % i       # minimum field
# Despliega el texto en el mínimo campo de escritura
print '"%5d"' % i      # field of width 5 characters
# Amplia el campo de escritura a 5 caracteres
print '"%05d"' % i     # pad with zeros
# 4 ceros aparecen antes de la variable que ocupa el 5 lugar
print '"%g"' % r       # r is big number so this is scientific notation
# Notación científica e
print '"%G"' % r       # E in the exponent
# Notación científica E
print '"%e"' % r       # compact scientific notation
# Notación científica con alta precisión e
print '"%E"' % r       # compact scientific notation
# Notación científica con alta precisión E
print '"%20.2E"' % r   # 2 decimals, field of width 20
# Notación científica desplegando solo 2 decimales y campo de escritura de 20 caracteres"
print '"%30g"' % r     # field of width 30 (right-adjusted)
# Campo de escritura 30 caracteres, ajustado a la derecha"
print '"%-30g"' % r    # left-adjust number
# Campo de escritura 30 caracteres, ajustado a la izquierda" 
print '"%-30.4g"' % r  # 3 decimals
# Campo de escritura de 30 caracteres ajustado a la izquierda con 4 decimales
print '%s' % i   # can convert i to string automatically
# Convierte numeros en caracteres automaticamente
print '%s' % r

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)
# Se utiliza para desplegar el signo de porcentaje

https://docs.python.org/2/library/math.html

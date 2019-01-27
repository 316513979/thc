
def tupla(M):
    Sf=[]
    Sc=[]
    I=len(M)
    E=len(M[0])
    s=0
    for fila in M:
        for n in fila:
            s=s+n
        Sf.append(s)
        s=0
    for elemento in range(E):
        for columna in range(I):
            s=s+M[columna][elemento]
        Sc.append(s)
        s=0
    T=(Sf, Sc)
    print 'La tupla resultante es: '
    print T
    
            
        
        
    
    
            
            

def lista_infinita(x):
    i=1
    while True:
        yield i*x
        i+= 1

for n in lista_infinita():
    print n
    
    

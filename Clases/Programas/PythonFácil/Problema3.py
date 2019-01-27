def primo(a):
    i=0
    E=range(1, a+1, 1)
    for entero in E:
        r=a%entero
        if r==0:
            i=i+1
    if a == 0:
        print '%d no es primo.' % (a)
    else:
        if 2<i:
            print '%d no es primo.' % (a)
        else:
            print '%d es primo.' % (a)

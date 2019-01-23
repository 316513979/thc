
# h = 4-(x**2)
L=[-1, 0, 1 ]
s=0
i=-1
while i < 1:
    j=i+1
    h1 = 4-(i**2)
    h2 = 4-(j**2)
    if h1<h2:
        a =h1
        s = s+a
    else:
        a=h1
        s=s+a
    i=i+1
print s
        


def mcd(a, b):
    r = a%b
    while r>0:
        a=b
        b=r
        r=a%b
    return b
            

#Intentos previos

#def mcd1(x, y):
 #   i=1
  #  while i<x and i<y:
   #     if (x/i)*i == (y/i)*i:
    #        print i
     #   else:
      #      i=i+1
            
#def divisores(x):
#    i=0
 #   while i<x:
  #      i=i+1
  #      if (x/i)*i == x:
 #       return

#a=10
#b=3
#s=a-b
#while s>0:
#	if s-b>0:
#		s=s-b
#		print s
#	else:
#		print s




    
            

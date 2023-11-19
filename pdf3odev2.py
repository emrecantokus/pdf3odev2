import math
x=2
j=0

while  j < 4:
    fonk=4*(math.e**(-0.5*x))-x
    fonk1=-2*(math.e**(-0.5*x))-1
    xc=x-(fonk/fonk1)
    x=xc
    j += 1
    
print("kok sonucu:")
print(xc)

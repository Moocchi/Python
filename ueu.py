from sympy import *

x = symbols ('x')
f =  (x**3*cos(x/2)+(1/2)*sqrt(4-x**2))
hasil = integrate(f,(x,-2,2))
print(float(hasil))

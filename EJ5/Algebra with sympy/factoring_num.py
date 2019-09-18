import sympy
import numpy

r1, r2, c2, epsilon, s = sympy.symbols('R_1 R_2 C_2 epsilon s') # To be printed in a latex style

num = sympy.Poly(-(20*c2**(2)*(epsilon**(2)-epsilon-5)*r1*r2**(2)*s**(2) + c2*(epsilon**(2)*r2+9*epsilon*r2-10*(3*r1+r2))*r2*s - 2*r1-r2), s)
print(sympy.solve(num, s))

num = sympy.Poly(-(2*r1 + r2 + s**2*(-20*c2**2*epsilon**2*r1*r2**2 + 20*c2**2*epsilon*r1*r2**2 + 10*c2**2*r1**2*r2 + 100*c2**2*r1*r2**2) + s*(-c2*epsilon**2*r2**2 - 9*c2*epsilon*r2**2 + c2*r1**2 + 31*c2*r1*r2 + 10*c2*r2**2)))
print(sympy.solve(num, s))
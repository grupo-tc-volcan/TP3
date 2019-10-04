import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
sym.init_printing(use_unicode=True)

r1, r2, r2p, r2pp, r3, c1, c2, psi, s = sym.symbols('R_{1} R_{2} R_{2}^{\'} R_{2}^{\'\'} R_{3} C_{1} C_{2} psi s') #Esto es para que me lo imprima para copiar y pegar en latex

r2p = r2*(psi)
r2pp = r2*(1-psi)
#r3 = r2*10
#c1 = c2*10

z1 = sym.factor((1/(s*c1))*(r2p)/(r2 + 1/(s*c1)))
z2 = sym.factor(((1/(s*c1))*(r2pp))/(r2 + 1/(s*c1)))
z3 = sym.factor((r2p*r2pp)/(r2 + 1/(s*c1)))

num = sym.factor((z3 + 1/(s*c2))*(z2 + r1 + r3)*r3/(z2 + r1 + r3 + z3 + 1/(s*c2)))
den = sym.factor((r1 + z1 + ((z3 + 1/(s*c2))*(z2 + r1 + r3)/(z2 + r1 + r3 + z3 + 1/(s*c2)))) * (z2 + r1 + r3))

Hs = num/den
Hs = Hs.subs((r2p + r2pp), r2)
Hs = sym.collect(sym.factor(Hs), s)
print("H(S) GENERAL:", Hs)
Hs = Hs.subs(c1, 10*c2)
Hs = sym.collect(sym.factor(Hs), s)
print("C1 = 10*C2: H(s) =", Hs)
#print('')
#print(num.as_poly())
from sympy import Symbol
from sympy import Function, simplify
from sympy import *
from sympy import init_printing
from sympy.core.numbers import pi, I, oo
from sympy import re, im
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers import solve
import matplotlib.pyplot as plt
import math
import numpy as np

WP = 10 * 2 * np.pi  #o 12Hz
F = 10000 #!!!!!!!!!
VCC = 15
A0 = 100000
VD = 1 #!!!!!!!!!!!
RD = 500000#SIMULAR Y VER!!!!!!!!!!!
R0 = 1#SIMULAR Y VER!!!!!!!!!!


#w = 2*np.pi*F

r1 = Symbol('R1',real = True, positive = True)
r3 = Symbol('R3',real = True, positive = True)
r4 = Symbol('R4',real = True, positive = True)
r5 = Symbol('R5',real = True, positive = True)
r6 = Symbol('R6',real = True, positive = True)
r7 = Symbol('R7',real = True, positive = True)
r8 = Symbol('R8',real = True, positive = True)
c2 = Symbol('C2',real = True, positive = True)
c6 = Symbol('C6',real = True, positive = True)
a = Symbol('A',real = True, positive = True)
#w = Symbol('w',real = True, positive = True)
#wp = Symbol ('Wpppp',real = True, positive = True)
f = Symbol('f',real = True, positive = True)
#vcc = Symbol('Vcc',real = True, positive = True)
#sr = Symbol('SR',real = True, positive = True)
#vp = Symbol('Vp',real = True, positive = True)
#vin = Symbol('Vin',real = True, positive = True)
vo = Symbol('Vo',real = True, positive = True)
raux = Symbol('Raux',real = True, positive = True)

def replaceValues (equation, case, a_):
    equation = equation.subs(a, a_)
    #equation = equation.subs(wp, WP/(2*np.pi))
    #equation = equation.subs(vcc, VCC)
    if case == 1:
        equation = equation.subs(r1, 2500)
        equation = equation.subs(r3, 2500)
        equation = equation.subs(r4, 10000)
    elif case == 2:
        equation = equation.subs(r1, 2500)
        equation = equation.subs(r3, 2500)
        equation = equation.subs(r4, 10000)
    elif case == 3:
        equation = equation.subs(r1, 25000)
        equation = equation.subs(r3, 25000)
        equation = equation.subs(r4, 100000)
    return simplify(equation)


s = Symbol('s')
aw = A0 / (1 + s/WP) #W or wp?

k= ((1/r4)+(1/r5)+(1/r8))
z2 = 1/(s*c2)
z6 = 1/(s*c6)
r7Pz6 = (1/((1/r7) + (1/z6)))#(r7 * z6)/(r7 + z6)
y1 = 1/r1
y2 = 1/z2
y3 = 1/r3
y4 = 1/r4
y5 = 1/r5
y6 = 1/r6
y7 = 1/r7
y8 = 1/r8
yk = 1/k
aux1 = (((1-y8) * yk)/(r7Pz6)) - ((yk*y8)*(y6+y1)) + (z2*yk*y8*(y3+y2))
aux2 = (yk*y4*(y6+y1)) - (z2*yk*y4*(y3+y2)) - (z2*y3) + (yk*y4)
h = aux1/aux2
result1 = factor(h)
result = simplify(result1)

# hMod = sqrt(re(h)**2 + im(h)**2)
# hMod = simplify(hMod)

print("h=")
print(result)
print("LATEX:")
print(latex(result.evalf()))
# result1 = replaceValues(h, 1, A0) #pasarle A0 o aw dependiendo de lo que quiera analizar.
# print("CASO 1>")
# print(latex(result1.evalf()))

###############################################
k=(y4+y5+y8)
k1=y6-z2*y3*y1+(1/r7Pz6)

num=(k/(k1*r7Pz6))-(y8)
denom=y4+((k*z2*y3*y1)/k1)

vovi=num/denom
result2 = factor(vovi)
result3 = simplify(result2)
print("vovi=")
print(result)
print("LATEX:")
print(latex(result3.evalf()))


#
# print("inverter: Vo/Vi=")
# result1 = replaceValues(h, 1, A0) #pasarle A0 o aw dependiendo de lo que quiera analizar.
# print("CASO 1>")
# print(latex(result1.evalf()))
#
# result2 = replaceValues(h, 2, A0) #pasarle A0 o aw dependiendo de lo que quiera analizar.
# print("CASO 2>")
# print(latex(result2.evalf()))
#
# result3 = replaceValues(h, 3, A0) #pasarle A0 o aw dependiendo de lo que quiera analizar.
# print("CASO3>")
# print(latex(result3.evalf()))
#
#
#
# print("VIN MAX:")
# vinm = (500000)/(sqrt(re(h)**2+im(h)**2)*s) #500000
# print("CASO 1>")
# vinmax = replaceValues(vinm, 1, aw)
# print(latex(vinmax.evalf()))
# print("CASO 2>")
# vinmax = replaceValues(vinm, 2, aw)
# print(latex(vinmax.evalf()))
# print("CASO 3>")
# vinmax = replaceValues(vinm, 3, aw)
# print(latex(vinmax.evalf()))
#
#
#
# #ESTO ES CONSIDERANDO R INTERNAS!-----------
# #r5 = (r4*R0)/(r4+R0)
# #vo = VD * ((a/R0 - 1/r2)/(1/r5 + 1/r2))
# #r6 = (vo*R0)/(VD*a)
# #raux =(r3 * (r2+((r5*r6)/(r5+r6))))/(r3+r2+((r5*r6)/(r5+r6)))
# #zin = r1 + (RD*raux)/(RD+raux)
# #HASTA ACAAAAAAAAAAAAA----------------------
#
# #CASO IDEAL:
# zin_sp = (a*r1 + r1 + r2)/(1+a)
# rp=10000000
# cp=1/(s * 12e-12)
# puntas = (rp * cp)/(rp+cp)
# zin = (puntas * zin_sp)/(puntas + zin_sp)
#
#
# expresion = simplify(zin)
# print("EXPRESION con puntas:")
# print(expresion)
#
# result = replaceValues(zin_sp, 1, aw)
# print("inverter: Zin caso1=")
# print(latex(result.evalf()))
#
# result = replaceValues(zin_sp, 2, aw)
# print("inverter: Zin caso2=")
# print(latex(result.evalf()))
#
# result = replaceValues(zin_sp, 3, aw)
# print("inverter: Zin caso3=")
# print(latex(result.evalf()))
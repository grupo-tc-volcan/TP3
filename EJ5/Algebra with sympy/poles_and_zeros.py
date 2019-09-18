import sympy
import numpy
import matplotlib.axes as axes
import matplotlib.pyplot as plt
import control

r1, r2, c2, epsilon, s = sympy.symbols('R_1 R_2 C_2 epsilon s') # To be printed in a latex style

num = sympy.Poly(-(20*c2**(2)*(epsilon**(2)-epsilon-5)*r1*r2**(2)*s**(2) + c2*(epsilon**(2)*r2+9*epsilon*r2-10*(3*r1+r2))*r2*s - 2*r1-r2), s)
den = sympy.poly(20*c2**(2)*(epsilon**(2)-epsilon-5)*r1*r2**(2)*s**(2) + c2*(epsilon**(2)*r2-11*epsilon*r2-31*r1)*r2*s - 2*r1-r2, s)

num = num.subs({r1:10, r2:1e3, c2:10e-9})
den = den.subs({r1:10, r2:1e3, c2:10e-9})

poles = []
zeros = []

p = 75
for i in range(1, p + 1):
    new_den = sympy.Poly(den.subs(epsilon, (i/p)), s)
    new_num = sympy.Poly(num.subs(epsilon, (i/p)), s)
    num_coeffs = list(new_num.coeffs())
    den_coeffs = list(new_den.coeffs())
    num_coeffs = [float(e) for e in num_coeffs]
    den_coeffs = [float(e) for e in den_coeffs]

    sys = control.tf(num_coeffs, den_coeffs)
    new_poles, new_zeros = control.pzmap(sys, Plot=False)
    poles.extend(new_poles)
    zeros.extend(new_zeros)

x_poles = [pole.real for pole in poles]
y_poles = [pole.imag for pole in poles]
x_zeros = [zero.real for zero in zeros]
y_zeros = [zero.imag for zero in zeros]

fig, (poles_plot, zeros_plot) = plt.subplots(1, 2)
fig.suptitle('Diagrama de polos y ceros')
poles_plot.scatter(x_poles, y_poles, marker='x', c='red')
zeros_plot.scatter(x_zeros, y_zeros, marker='o', c='blue')

poles_plot.set_xlabel('Parte real σ (Hz)')
poles_plot.set_ylabel('Parte imaginaria jω (Hz)')
poles_plot.set_title('Polos')
poles_plot.ticklabel_format(axis='both', scilimits=(-2,2))
poles_plot.grid()
poles_plot.autoscale()

zeros_plot.set_xlabel('Parte real σ (Hz)')
zeros_plot.set_ylabel('Parte imaginaria jω (Hz)')
zeros_plot.set_title('Ceros')
zeros_plot.ticklabel_format(axis='both', scilimits=(-2,2))
zeros_plot.grid()
zeros_plot.autoscale()

plt.show()
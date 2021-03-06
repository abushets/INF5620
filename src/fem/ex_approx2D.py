"""
Examples on approximating functions by global basis functions,
using the approx2D.py module.
"""
from approx2D import *
import sympy as sm
import sys
x, y = sm.symbols('x y')


def sines(x, y, Nx, Ny):
    return [sm.sin(sm.pi*(i+1)*x)*sm.sin(sm.pi*(j+1)*y)
            for i in range(Nx+1) for j in range(Ny+1)]

def taylor(x, y, Nx, Ny):
    return [x**i*y**j for i in range(Nx+1) for j in range(Ny+1)]


# ----------------------------------------------------------------------

def run_linear():
    f = (1+x**2)*(1+2*y**2)
    phi = taylor(x, y, 1, 1)
    print phi
    Omega = [[0, 2], [0, 2]]
    u = least_squares(f, phi, Omega)
    comparison_plot(f, u, Omega, plotfile='approx2D_bilinear')
    print '\n\n**** Include second order terms:'
    phi = taylor(x, y, 2, 2)
    u = least_squares(f, phi, Omega)


if __name__ == '__main__':
    functions = \
        [eval(fname) for fname in dir() if fname.startswith('run_')]
    from scitools.misc import function_UI
    cmd = function_UI(functions, sys.argv)
    eval(cmd)

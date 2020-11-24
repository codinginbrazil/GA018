''' Método de Newton: encontrar o mínimo dessa função '''

from sympy import lambdify, diff, cos, sin
from sympy.abc import x

from Error import * 
from Log import *


MAX = 50
PATH = 'log/newton/'
TOLERANCE = 0.00000001 # 10**(-8)

                                 
def newton(fn, cx, tol, nmax, log) :
    e = Error()
    previous = 0
    
    dx = fn.diff(x)
    dx = lambdify(x, dx)
    fn = lambdify(x, fn)
     
    for n in range(nmax) : 
        if (dx(cx) == 0) :
            return "Error 25: derivative less than zero"
            breakpoint
        cx = cx - (fn(cx) / dx(cx) )
        e.absolute(cx, previous)
        e.relative(cx, previous)
        log.append([cx, e._absolute, e._relative, fn(cx), dx(cx)])
        if (e._absolute < tol) :
            return cx
            breakpoint
        previous = cx
    return False


def run_test(function, a, TOLERANCE, MAX): 
    log = []
    m = newton(function, a, TOLERANCE, MAX, log)
    
    l = Log(log)
    l.set_header(['x='+str(a), 'absolute_error', 'relative_error', 'function', 'derivative'])
    l.list2file((PATH+str(function)))

    print('f(x) =',f, '-> newton optimization =', m)



if __name__ == "__main__":
    ''' Tests '''
    a = 0.5
    fx = [(cos(x) - x**3), (x**2 - 612), ((x**3)-(2*x)+2), (x**6 - x - 1)]
    
    for f in fx:
        run_test(f, a, TOLERANCE, MAX)
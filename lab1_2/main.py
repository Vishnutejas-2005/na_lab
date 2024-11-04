

def f_bi(x):
    return (x**3)-(7*(x**2))+(14*x)-6




def bisection_method_sir(f,a,b,N0 = 1000,tol = 10**-4):
    i = 1
    fa = f(a)
    if fa*f(b) >0:
        return  "f(a) and f(b) have the same sign"
    while i<=N0:
        p = a +  ((b-a)/2)
        fp = f(p)
        if fp == 0 or (b-a)/2 < tol:
            return p
        i+=1
        if fa*fp >0:
            a = p
            fa = fp
        else:
            b = p
        
    return f"Method Faliure after {N0} iterations"

# print(bisection_method_sir(f_bi,3.2,4))


def g_fpi(x):
    return (3*((x**2)+1))**0.25

def fixed_point_iteration(g,p0,n0 = 1000,tol = 10**-2):
    i = 1
    while i<=n0:
        p = g(p0)
        if abs(p-p0)<tol:
            return p
        i = i+1
        p0 = p
    return f"Method Faliure after {n0} iterations"

print(fixed_point_iteration(g_fpi,1))



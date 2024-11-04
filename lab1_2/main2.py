from math import e,log
def f_new_1(x):
    return (x**3)-(2*(x**2))-5

def df_1(x):
    return (3*(x**2))-(4*x)

def df_2(x):
    return (2*x)-(2*(e**(-x))) + (2*x*(e**(-x))) -(2*(e**(-2*x)))

def f_new_2(x):
    return (x**2)-(2*(x)*(e**(-x)))+(e**(-(2*x)))

def f_new_3(x):
    return (x**3)- (3*(x**2)*(2**(-x)))+(3*x*(4**(-x)))-(8**(-x))

def df_3(x):
    return 3*x**2-6*x*2**(-x)+3*(x**2)*2**(-x)*log(2)+3*4**(-x)-3*x*4**(-x)*log(4)+8**(-x)*log(8)

def newton(f,df,p0,N0 = 1000,tol = 10**-5):
    i = 1
    while i<= N0 :
        p = p0 - (f(p0)/df(p0))
        if abs(p-p0)<tol:
            return p
        i+=1
        p0 = p
    return f"Method Faliure after {N0} iterations"

# print(newton(f_new_1,df_1,4))
# print(newton(f_new_2,df_2,0.5))
# print(newton(f_new_3,df_3,0.5))

def f(x):
    return (230*(x**4))+(18*(x**3))+(9*(x*x))-(221*(x))-9

def df(x):
    return (4*(230*(x**3)))+(3*(18*(x**2)))+(2*(9*(x)))-(221)

def secant(f,p0,p1,N0 = 1000,tol = 10**-6):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= N0:
        p = p1 - q1*((p1-p0)/(q1-q0))
        if abs(p-p1)<tol:
            return p
        i+=1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    return f"Method Faliure after {N0} iterations"


# print(secant(f,-1,0))
# print(secant(f,0,1))
# print(secant(f,0.5,1))


    
def false_position(f,po,p1,TOL= 10**-6):
    qo = f(po)
    q1 = f(p1)
    p = p1 - q1*((p1 - po)/(q1-qo))
    while abs(p-p1)>TOL:
        q = f(p)
        if q*q1 <0:
            po = p1 
            qo = q1
        p1 = p
        q1 = q
        p = p1 - q1*((p1 - po)/(q1-qo))
    return p
    

print(false_position(f,-1,0))
print(false_position(f,0,1))


import math
from numpy import zeros, linspace
#Adams-Bashforth 3/Moulton 4 Step Predictor/Corrector
#Runge-Kutta "Classic" Order 4 method
def RK4(t0,tn,n,y0):
    h = abs(tn-t0)/n
    t = linspace(t0,tn,n+1)
    y = zeros(n+1)
    y[0] = y0
    for i in range(0,n):
        K1 = f(t[i],y[i])
        K2 = f(t[i]+h/2,y[i]+K1*h/2)
        K3 = f(t[i]+h/2,y[i]+K2*h/2)
        K4 = f(t[i]+h,y[i]+K3*h)
        y[i+1] = y[i] + h*(K1+2*K2+2*K3+K4)/6
    return y
def f(t,y):
    return y-t**2+1
#Adams-Bashforth 3/Moulton 4 Step Predictor/Corrector
def PreCorr3(t0,tn,n,y0):
    h = abs(tn-t0)/n
    t = linspace(t0,tn,n+1)
    y = zeros(n+1)
    #Calculate initial steps with Runge-Kutta 4
    y[0:3] = RK4(t0,t0+2*h,2,y0)
    K1 = f(t[1],y[1])
    K2 = f(t[0],y[0])
    for i in range(2,n):
        K3 = K2
        K2 = K1
        K1 = f(t[i],y[i])
        #Adams-Bashforth Predictor
        y[i+1] = y[i] + h*(23*K1-16*K2+5*K3)/12
        K0 = f(t[i+1],y[i+1])
        #Adams-Moulton Corrector
        y[i+1] = y[i] + h*(9*K0+19*K1-5*K2+K3)/24
    return y
def g(t):
    return (t+1)**2-0.5*math.exp(t)

print(PreCorr3(0,2,10,0.5))
print(g(2))
print(g(2)-PreCorr3(0,2,10,0.5)[10])
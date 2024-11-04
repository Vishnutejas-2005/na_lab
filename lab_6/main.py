import math 
def f1(x,y):
    return (y/x)-((y*y)/(x*x))

def y1(x):
    return x/(1+math.log(x))

# def f2(x,y):
#     return ((y*y)+y)

def RK_2(x0,y0,h,xn):
    n = int((xn-x0)/h)+1

    print(n)
    y = y0
    x = x0
    list_of_yi = [(x,y)]
    for i in range(n):
        print(i)
        k1 = h*f1(x,y)
        k2 = h*f1(x+(h),y+(k1))
        y = y + (k1+k2)/2
        x = x + h
        list_of_yi.append((x,y))
    
    return list_of_yi

print(RK_2(1,1,0.1,1.2))

def RK_2_mid_point(x0,y0,h,xn):
    n = int((xn-x0)/h)+1

    print(n)
    y = y0
    x = x0
    list_of_yi = [(x,y)]
    for i in range(n):
        print(i)
        k1 = h*f1(x,y)
        k2 = h*f1(x+(h/2),y+(k1/2))
        y = y + k2
        x = x + h
        list_of_yi.append((x,y))
    
    return list_of_yi

# print(RK_2_mid_point(1,1,0.1,1.2))

def g1(x0,x1,y0,h,y):
    return y0 + h*((f1(x0,y)+f1(x1,y0))/2)

def fixed_point_iteration(x0,x1,y0,h,tol = 10**-2,max_iter = 100000000):
    print("Fixed Point Iteration")
    print(f"X0: {x0}\n X1: {x1}\n Y0: {y0}\n h: {h}")
    i = 0
    y = y0
    while i<max_iter:
        i += 1
        y1 = g1(x0,x1,y0,h,y)
        if abs(y1-y0)<tol:
            return y1
        y1 = y0
    print("Max Iteration Reached")


def trapezoidal(x0,y0,h,xn):
    n = int((xn-x0)/h)+1

    print(n)
    y = y0
    x = x0
    list_of_yi = [(x,y)]

    for i in range(n):
        print(i)
        y = fixed_point_iteration(x,x+h,y,h)
        x = x + h
        list_of_yi.append((x,y))

    return list_of_yi


print(trapezoidal(1,1,0.05,1.2))

def f_dash_1(x,y):
    return f1(x,y)*((x-(2*y))/x**2)-(y/(x**2))+2*((y**2)/(x**3))

def taylors_order_2(x0,y0,h,xn):
    n = int((xn-x0)/h)+1

    print(n)
    y = y0
    x = x0
    list_of_yi = [(x,y)]

    for i in range(n):
        print(i)
        y = y + h*f1(x,y) + (h*h*f_dash_1(x,y))/2
        x = x + h
        list_of_yi.append((x,y))

    return list_of_yi

# print(taylors_order_2(1,1,0.1,1.2))
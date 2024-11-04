from math import e
def f1(x, y):
    return x*(e**(3*x))-2*y


def euler_method(x0,y0,h,xn):
    n = int((xn - x0)/h)
    print(n)
    x = x0
    y = y0
    list_of_yi = [(x0,y0)]
    for i in range(n):
        y = y + h*f1(x, y)
        x = x + h
        list_of_yi.append((x,y))
    return list_of_yi

print(euler_method(0,0,0.5,1))
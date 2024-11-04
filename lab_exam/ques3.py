from math import e,sin,pi,tan
def f(x):
    return (e**x)+(3*(x**2)) 

def simpson(a,b):
    return ((b-a)/6)*(f(a)+(4*f((a+b)/2))+f(b))


def composite_simpson(a,b):
    n = 1
    while True:
        print(n)
        h = (b-a)/n
        list_of_x = [a+(i*h) for i in range(n+1)]
        sum = 0
        for i in range(len(list_of_x)-1):
            sum += simpson(list_of_x[i],list_of_x[i+1])
        if abs(sum - e) < 10**-6:
            return sum,n,list_of_x
        n+=1
print(composite_simpson(0,1))

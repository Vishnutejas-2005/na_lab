from math import e,sin,pi,tan
# def f(x):
#     # return (2/(x-4))
#     # return (e**(3*x))*sin(2*x)
#     # return (x**3)*(e**x)
#     # return tan(x)
#     return 2**x

# def simpson(a,b):
#     return ((b-a)/6)*(f(a)+(4*f((a+b)/2))+f(b))


# # print(simpson(0, 0.5))
# # print(simpson(0,(pi/4)))
# def composite_simpson(a,b,n):
#     h = (b-a)/n
#     list_of_x = [a+(i*h) for i in range(n+1)]
#     sum = 0
#     for i in range(len(list_of_x)-1):
#         sum += simpson(list_of_x[i],list_of_x[i+1])
#     return sum

# print(composite_simpson(0, 8, 4))


# print(((pi/8)*2)*sin(pi/8)*(pi/4))

print((16 - (pi**2) +(8*pi)-(32*(2**0.5)))/(16*(2**0.5)))
from math import e

def f_1(x,y):
    return y - x**2 + 1

def y_1_real(x):
    return (x +1)**2 - (e**x)/2

def RK_2(x0,y0,h,n,f1):
    y = y0
    x = x0
    list_of_yi = [y]
    list_of_xi = [x]
    for i in range(n):
        k1 = h*f1(x,y)
        k2 = h*f1(x+(h),y+(k1))
        y = y + (k1+k2)/2
        # i want to round of till 2 decml places

        x = round(x + h,2)
        list_of_yi.append(y)
        list_of_xi.append(x)
    
    return list_of_xi, list_of_yi

def RK_4(x0,y0,h,n,f1):
    y = y0
    x = x0
    list_of_yi = [y]
    list_of_xi = [x]
    for i in range(n):
        k1 = h*f1(x,y)
        k2 = h*f1(x+(h/2),y+(k1/2))
        k3 = h*f1(x+(h/2),y+(k2/2))
        k4 = h*f1(x+h,y+k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6
        x = round(x + h,2)
        list_of_yi.append(y)
        list_of_xi.append(x)
    
    return list_of_xi, list_of_yi

# print(RK_2(0,0,0.1,10,f_1))

def adam_bashforth(x,y,f, xn,h,order):

    n = int(round((xn-x[0])/h,2))
    for _ in range(n-order+1):
        if order == 2:
            y.append(y[-1] + h*(3*f(x[-1],y[-1]) - f(x[-2],y[-2]))/2)
        elif order == 3:
            y.append(y[-1] + h*(23*f(x[-1],y[-1]) - 16*f(x[-2],y[-2]) + 5*f(x[-3],y[-3]))/12)
        elif order == 4:
            y.append(y[-1] + h*(55*f(x[-1],y[-1]) - 59*f(x[-2],y[-2]) + 37*f(x[-3],y[-3]) - 9*f(x[-4],y[-4]))/24)
        else:
            print("Invalid order")
            return None
        x.append(round(x[-1] + h,2))

    return x,y



def problem_1_ab():
    x0 = 0
    y0 = 0.5
    xn = 2
    h = 0.2
    n = 1
    order = 2
    x,y = RK_2(x0,y0,h,n,f_1)
    x,y = adam_bashforth(x,y,f_1,xn,h,order)
    print(x)
    print(y)

def problem_1_actual():
    x0 = 0
    y0 = 0.5
    xn = 2
    h = 0.2
    n = int((xn - x0)/h)
    x = [round(x0 + i*h,2) for i in range(n+1)]
    y = [y0]

    for i in range(1,n+1):
        y.append(y_1_real(x[i]))

    print(x)
    print(y)


problem_1_ab()



def adam_moulton_fixed_point(x,y,f, xn,h,order):

    n = int((xn-x[0])/h)
    tol = 10**-5
    for _ in range(n-order+1):
        if order == 2:
            x1 = round(x[-1] + h,2)
            y1 = y[-1] 
            while True:
                y_new = y[-1]+h/12*(5*f(x1,y1)+8*f(x[-1],y[-1])-f(x[-2],y[-2]))
                if abs(y_new - y1) < tol:
                    break
                y1 = y_new
            y.append(y_new)
        elif order == 3:
            x1 = round(x[-1] + h,2)
            y1 = y[-1] 
            while True:
                y_new = y[-1]+h*(9*f(x1,y1)+19*f(x[-1],y[-1])-5*f(x[-2],y[-2])+f(x[-3],y[-3]))/24
                if abs(y_new - y1) < tol:
                    break
                y1 = y_new
            y.append(y_new)
        elif order == 4:
            x1 = round(x[-1] + h,2)
            y1 = y[-1] 
            while True:
                y_new = y[-1]+h/720*(251*f(x1,y1)+646*f(x[-1],y[-1])-264*f(x[-2],y[-2])+106*f(x[-3],y[-3])-19*f(x[-4],y[-4]))
                if abs(y_new - y1) < tol:
                    break
                y1 = y_new
            y.append(y_new)
        else:
            print("Invalid order")
            return None
        x.append(round(x[-1] + h,2))

    return x,y



def problem_2_am():
    x0 = 0
    y0 = 0.5
    xn = 2
    h = 0.2
    n = 1
    order = 2
    x,y = RK_2(x0,y0,h,n,f_1)
    x,y = adam_moulton_fixed_point(x,y,f_1,xn,h,order)
    print(x)
    print(y)

problem_2_am()
problem_1_actual()

def problem_3_a():
    x0 = 0
    y0 = 0.5
    xn = 2
    h = 0.2
    n = 2
    order = 3
    x,y = RK_2(x0,y0,h,n,f_1)
    x,y = adam_bashforth(x,y,f_1,xn,h,order)
    print(x)
    print(y)


problem_3_a()

def problem_3_b():
    x0 = 0
    y0 = 0.5
    xn = 2
    h = 0.2
    n = 2
    order = 3
    x,y = RK_2(x0,y0,h,n,f_1)
    x,y = adam_moulton_fixed_point(x,y,f_1,xn,h,order)
    print(x)
    print(y)

problem_3_b()

def predictor_corrector_4(x,y,f, xn,h):

    n = int((xn-x[0])/h)
    tol = 10**-5
    for _ in range(n-4):
        x1 = round(x[-1] + h,2)
        y1 = y[-1] + h*(55*f(x[-1],y[-1]) - 59*f(x[-2],y[-2]) + 37*f(x[-3],y[-3]) - 9*f(x[-4],y[-4]))/24
        y1 = y[-1]+h*(251*f(x1,y1)+646*f(x[-1],y[-1])-264*f(x[-2],y[-2])+106*f(x[-3],y[-3])-19*f(x[-4],y[-4]))/720
        y.append(y1)
        x.append(x1)
        
        
    return x,y

def problem_4():
    x0 = 0
    y0 = 0.5
    xn = 2
    h = 0.2
    n = 4
    x,y = RK_4(x0,y0,h,n,f_1)
    x,y = predictor_corrector_4(x,y,f_1,xn,h)
    print(x)
    print(y)

problem_4()







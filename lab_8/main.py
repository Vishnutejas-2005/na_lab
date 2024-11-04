# shooting problem
# system of ODE for 2nd order differential method

from math import e, sin,log,cos

# converting 2nd order differential equation into system of ode
# def f1(t,u,v):
#     return v
# def f2(t,u,v):
#     return (2*v) - (2*u) + ((sin(t))*(e**(2*t)))
def f1(t,u,v):
    return v
def f2(t,u,v):
    return (-2*v)/t + (2*u)/(t**2) +  sin(log(t))/(t**2)

def f_actual(t):
    return 1.13921*t - 0.03921/(t**2) - 0.3*sin(log(t))-0.1*cos(log(t))

def f2_b(t,u,v):
    return (-2*v)/t + (2*u)/(t**2)

def RK_2_system(t0,U0,h,f1,f2,tn):
    u = U0[0]
    v = U0[1]
    t = t0
    list_of_u = [u]
    list_of_v = [v]
    list_of_t = [t]
    n = int(round((tn-t0)/h,2))
    for i in range(n):
        k1 = h*f1(t,u,v)
        l1 = h*f2(t,u,v)
        k2 = h*f1(t+(h),u+(k1),v+(l1))
        l2 = h*f2(t+(h),u+(k1),v+(l1))
        u = u + (k1+k2)/2
        v = v + (l1+l2)/2
        t = round(t + h,2)
        list_of_u.append(u)
        list_of_v.append(v)
        list_of_t.append(t)
    
    return list_of_t, list_of_u, list_of_v

def RK_4_system(t0,U0,h,f1,f2,tn):
    u = U0[0]
    v = U0[1]
    t = t0
    list_of_u = [u]
    list_of_v = [v]
    list_of_t = [t]
    n = int(round((tn-t0)/h,2))
    for i in range(n):
        k1 = h*f1(t,u,v)
        l1 = h*f2(t,u,v)
        k2 = h*f1(t+(h/2),u+(k1/2),v+(l1/2))
        l2 = h*f2(t+(h/2),u+(k1/2),v+(l1/2))
        k3 = h*f1(t+(h/2),u+(k2/2),v+(l2/2))
        l3 = h*f2(t+(h/2),u+(k2/2),v+(l2/2))
        k4 = h*f1(t+h,u+k3,v+l3)
        l4 = h*f2(t+h,u+k3,v+l3)
        u = u + (k1 + 2*k2 + 2*k3 + k4)/6
        v = v + (l1 + 2*l2 + 2*l3 + l4)/6
        t = round(t + h,2)
        list_of_u.append(u)
        list_of_v.append(v)
        list_of_t.append(t)
    
    return list_of_t, list_of_u, list_of_v


def ques5():
    t0 = 1
    U0 = [1,0]
    h = 0.1
    tn = 2
    beta = 2
    # a,b,c = RK_2_system(t0,U0,h,f1,f2,tn)
    d,e,f = RK_4_system(t0,U0,h,f1,f2,tn)
    # x =[]
    # for i in a:

    #     x.append(f(i))
    # print(a)
    # print(b)
    # print(c)
    print(d)
    print(e)
    print(f)
    # print(x)
    U1 = [0,1]
    g,h,i = RK_4_system(t0,U1,h,f1,f2_b,tn)
    print(g)
    print(h)
    print(i)
    approx_function_values = []
    for k in range(len(d)):
        approx_function_values.append(e[k]+ ((beta-e[-1])/h[-1])*h[k])

    print(approx_function_values)
    func_values= []
    for t in range(len(d)):
        x = d[t]
        y = f_actual(x)
        func_values.append(y)
    print(func_values)


# ques5()









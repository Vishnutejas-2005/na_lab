# applying shooting method using newton method for solving the boundary value problem


def func1(t,u,v):
    return u

def func2(t,u,v):
    return (32 + (2*(t**3)) - (u*v))/8

def derivative_func1_u(t,u,v):
    pass

def RK_4_system(t0,U0,h,f1,f2,n):
    u = U0[0]
    v = U0[1]
    t = t0
    list_of_u = [u]
    list_of_v = [v]
    list_of_t = [t]
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


def ques_2():
    M = 10
    N = 20
    t0 = 1
    tn = 3
    beta = 43/3
    alpha = 7
    h = round((tn - t0)/N,2)
    initial_approx_y_dash = 1

    for i in range(M):
        U0 = [alpha, initial_approx_y_dash]
        t,u,v = RK_4_system(t0,U0,h,func1,func2,N)
        

#newton raphson method for system of equations

def f1(x,y):
    return x**2 - y
def f2(x,y):
    return x - y

def f(x,y):
    return [f1(x,y),f2(x,y)]

def jacobian(x,y):
    return [[2*x,-1],[1,-1]]

def jacobian_inverse(x,y):
    j = jacobian(x,y)
    det = j[0][0]*j[1][1] - j[0][1]*j[1][0]
    return [[j[1][1]/det,-j[0][1]/det],[-j[1][0]/det,j[0][0]/det]]

def newton_raphson(x0,y0,N0 = 1000,tol = 10**-10):
    i = 1
    while i <= N0:
        p = [x0,y0]
        j = jacobian_inverse(x0,y0)
        p[0] = x0 - (j[0][0]*f1(x0,y0) + j[0][1]*f2(x0,y0))
        p[1] = y0 - (j[1][0]*f1(x0,y0) + j[1][1]*f2(x0,y0))
        print(i)
        print(p)

        # if abs(p[0]-1)<tol and abs(p[1]-1)<tol:
        #     return p,i
        if ((abs(p[0]-1))**2 + (abs(p[1]-1))**2)**0.5 < tol:
            return p,i
        i+=1
        x0 = p[0]
        y0 = p[1]

print(newton_raphson(1.5,1.5))
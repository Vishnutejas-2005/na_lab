def secant(f,p0,p1,N0 = 1000,tol = 10**-6):
    sol = 2**0.5
    print(sol)
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= N0:
        print(i)
        p = p1 - q1*((p1-p0)/(q1-q0))
        print(p)
        if abs(p-sol)<tol:
            return p,i
        i+=1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    return f"Method Faliure after {N0} iterations"

def f(x):
    return (x**2)-2

print(secant(f,1,2))
from math import e,sin,log,cos
import numpy as np

a = 2
b = 0
c = 0

def y(x):
    return 64*(x**2)*((1-x)**2)

def f(x):
    return -a*(128-(768*x)+(768*(x**2))) + ((b + (c*(x**2)))*y(x))

def g(x):
    return b + (c*(x**2))

def actual_solution(x):
    return 64*(x**2)*((1-x)**2)

def finite_difference(f,g,a0,b0,n,alpha,beta):
    h = (b0-a0)/(n+1)
    x = np.linspace(a0+h,b0-h,n)
    A = np.zeros((n,n))
    b = np.zeros(n)
    b[0] = (h**2)*f(x[0]) + a*alpha
    b[n-1] = (h**2)*f(x[n-1]) + a*beta
    for i in range(n):
        A[i,i] = 2*a + g(x[i])*(h**2)
        if i > 0:
            A[i,i-1] = -a
        if i < n-1:
            A[i,i+1] = -a
    for i in range(1,n-1):
        b[i] = (h**2)*f(x[i])
    return A,b

A1,b1 = finite_difference(f,g,0,1,9,0,0)
A2,b2 = A1,b1
print(A1)
print(b1)

def gauss_jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = np.copy(x0)
    x_new = np.zeros(n)
    for k in range(max_iter):
        for i in range(n):
            x_new[i] = b[i]
            for j in range(n):
                if j != i:
                    x_new[i] -= A[i, j] * x[j]
            x_new[i] /= A[i, i]
        if np.linalg.norm(x_new - x) < tol:
            return x_new,k
        x = np.copy(x_new)

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = np.copy(x0)
    x_new = np.zeros(n)
    for k in range(max_iter):
        for i in range(n):
            x_new[i] = b[i]
            for j in range(n):
                if j < i:
                    x_new[i] -= A[i, j] * x_new[j]
                elif j > i:
                    x_new[i] -= A[i, j] * x[j]
            x_new[i] /= A[i, i]
        if np.linalg.norm(x_new - x) < tol:
            return x_new,k
        x = np.copy(x_new)
    return "hi"
    

jacobi_sol,no_of_iter_1 = gauss_jacobi(A1,b1,[0,0,0,0,0,0,0,0,0],1e-5,5000)
seidel_sol,no_of_iter_2 = gauss_seidel(A2,b2,[0,0,0,0,0,0,0,0,0],1e-5,5000)
print("jacobi solution")
print(jacobi_sol)
print(no_of_iter_1)
print("seidel solution")
print(seidel_sol)
print(no_of_iter_2)
# i want to plot the actual solution and the numerical solution
import matplotlib.pyplot as plt
h =0.1
x = np.linspace(0+h,1-h,9)
actual = [actual_solution(i) for i in x]
# # on th same plot plot the numerical solution
# plt.plot(x,jacobi_sol)
# # plt.plot(x,actual)
# plt.plot(x,seidel_sol)
# plt.show()
print("actual solution")
print(actual)
def error(actual,numerical):
    return np.linalg.norm(actual-numerical,ord=np.inf)

print("error for jacobi")
print(error(np.array(actual),jacobi_sol))
print("error for seidel")
print(error(np.array(actual),seidel_sol))
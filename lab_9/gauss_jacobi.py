from math import e,sin,log,cos
import numpy as np
def gaussian_elimination(A, b):
    n = len(b)
    for i in range(n):
        if A[i, i] == 0:
            # find the first row with non-zero element in the i-th column and swap
            for j in range(i+1, n):
                if A[j, i] != 0:
                    for k in range(i, n):
                        A[i, k], A[j, k] = A[j, k], A[i, k]
                    b[i], b[j] = b[j], b[i]
                    break
            # if all elements in the previous iteration A[j,i]==0 then raise an error
            if A[i, i] == 0:
                raise ValueError("Matrix is singular")
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    x = np.zeros(n)
    if A[n-1, n-1] == 0:
        if b[n-1] == 0:
            raise ValueError("Infinite solutions")
        else:
            raise ValueError("No solution")
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
    return x


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
        if (np.linalg.norm(x_new - x,ord=np.inf)/np.linalg.norm(x_new,ord=np.inf)) < tol:
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
        if (np.linalg.norm(x_new - x,ord=np.inf)/np.linalg.norm(x_new,ord=np.inf)) < tol:
            return x_new,k
        x = np.copy(x_new)


A = np.array([[4,-1,1], [2,5,2], [1,2,4]])
b = np.array([8,3,11])
# cast the matrix to float
A = A.astype(float)
b = b.astype(float)

print(gaussian_elimination(A,b))


A2 = np.array([[10,-1,2,0], [-1,11,-1,3], [2,-1,10,-1],[0,3,-1,8]])
b2 = np.array([6,25,-11,15])
# cast the matrix to float
A2 = A2.astype(float)
b2 = b2.astype(float)

print(gauss_jacobi(A2,b2,[0,0,0,0],1e-3,100))

# linear finite difference problem

def p(x):
    return -2/x

def q(x):
    return 2/(x**2)

def r(x):
    return sin(log(x))/(x**2)

def actual_solution(x):
    return 1.13921*x-0.03921/(x**2)-0.3*sin(log(x))-0.1*cos(log(x))

def finite_difference(p,q,r,a,b,n,alpha,beta):
    h = (b-a)/(n+1)
    x = np.linspace(a+h,b-h,n)
    A = np.zeros((n,n))
    b = np.zeros(n)
    b[0] = -h**2*r(x[0]) + (1 + h*p(x[0])/2)*alpha
    b[n-1] = -h**2*r(x[n-1]) + (1 - h*p(x[n-1])/2)*beta
    for i in range(n):
        A[i,i] = 2 + h**2*q(x[i])
        if i > 0:
            A[i,i-1] = -1 - h*(p(x[i])/2)
        if i < n-1:
            A[i,i+1] = -1 + h*(p(x[i])/2)
    for i in range(1,n-1):
        b[i] = -h**2*r(x[i])
    return A,b

a = 1
b = 2
n = 9
alpha = 1
beta = 2
A,b = finite_difference(p,q,r,a,b,n,alpha,beta)
print(A)
print(b)
# print("gaussian_elimination")
# print(gaussian_elimination(A,b))
# print(A)
# print(b)
print("gauss_jacobi")
print(gauss_jacobi(A,b,np.zeros(n),1e-5,10000000))
print(A)
print(b)
# print("gauss_seidel")
# print(gauss_seidel(A,b,np.zeros(n),1e-3,100))
# print(A)
# print(b)

# h = (2-a)/(n+1)
# x = np.linspace(a+h,2-h,n)
# print("actual solution")
# for i in x:
#     print(actual_solution(i))

# # print(A)
# print(b)

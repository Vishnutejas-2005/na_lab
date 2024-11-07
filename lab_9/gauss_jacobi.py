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
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    x = np.zeros(n)
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
# # check if the method converges
# # 2*2 matrix
# A = np.array([[2, 1], [5, 7]])
# b = np.array([6, 24])
# x0 = np.array([0, 0])
# tol = 1e-10
# max_iter = 100
# x,k = gauss_jacobi(A, b, x0, tol, max_iter)
# print(x,k)

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




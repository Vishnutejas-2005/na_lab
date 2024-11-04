
def forward_differences(x_samples, y_samples):
    n = len(x_samples)
    divided_differences = []
    divided_differences.append(y_samples)
    difference_num = 1
    while True :
        new_row = []
        for i in range(len(divided_differences[-1])-1):
            new_row.append((divided_differences[-1][i+1] - divided_differences[-1][i]) / (x_samples[i+difference_num] - x_samples[i]))
        divided_differences.append(new_row)
        difference_num += 1
        if len(new_row) == 1:
            break
    return divided_differences


def interpolating_polynomial(x_samples, y_samples):
    n = len(x_samples)
    divided_differences = forward_differences(x_samples, y_samples)
    polynomial = ""
    for i in range(n):
        if divided_differences[i][0]!=0:
            polynomial += str(divided_differences[i][0])
            for j in range(i):
                polynomial += "*(x - " + str(x_samples[j]) + ")"
            if i != n-1:
                polynomial += " + "
    polynomial += "+ 0"
    return polynomial

# polynomial = interpolating_polynomial([1, 2, 3,4], [1, 4,9,16])
# print(polynomial)   


def evaluate_polynomial(polynomial_str, x_value):
    # Replace 'x' with the actual x_value in the polynomial string
    polynomial_str = polynomial_str.replace('x', str(x_value))
    # Evaluate the polynomial string
    return eval(polynomial_str)

# # # Example usage
# # # x = [-0.75,-0.5,-0.25,0]
# # # y = [-0.07181250,-0.02475,0.3349375,1.101000]
# # # print("points interpolated:", x, y)
# # # polynomial = interpolating_polynomial(x,y)
# # # print("Polynomial:", polynomial)

# # # # Evaluate the polynomial at x = 2
# # # value_at_p = evaluate_polynomial(polynomial, -1/3)
# # # print("Value at x=-1/3:", value_at_p)


# # # x = [-0.5,-0.25,0.0]
# # # y = [-0.02475,0.3349375,1.101000]
# # # print("points interpolated:", x, y)
# # # polynomial = interpolating_polynomial(x,y)
# # # print("Polynomial:", polynomial)

# # # # Evaluate the polynomial at x = 2
# # # value_at_p = evaluate_polynomial(polynomial, -1/3)
# # # print("Value at x=-1/3:", value_at_p)


# # # x = [-0.75,-0.5,-0.25]
# # # y = [1.101000,0.3349375,-0.02475]
# # # print("points interpolated:", x, y)
# # # polynomial = interpolating_polynomial(x,y)
# # # print("Polynomial:", polynomial)

# # # # Evaluate the polynomial at x = 2
# # # value_at_p = evaluate_polynomial(polynomial, -1/3)
# # # print("Value at x=-1/3:", value_at_p)


# x = [-2,-1,0,1,2,3]
# y = [1,4,11,16,13,-4]
# print("points interpolated:", x, y)
# polynomial = interpolating_polynomial(x,y)
# print("Polynomial:", polynomial)

# # Evaluate the polynomial at x = 2
# value_at_p = evaluate_polynomial(polynomial, 0.25)
# print("Value at x=0.25:", value_at_p)
# # print("")
# x = [0.1,0.2,0.3]
# y = [-0.062049958,-0.28398668,0.00660095]
# print("points interpolated:", x, y)
# polynomial = interpolating_polynomial(x,y)
# print("Polynomial:", polynomial)

# # Evaluate the polynomial at x = 2
# value_at_p = evaluate_polynomial(polynomial, 0.25)
# print("Value at x=0.25:", value_at_p)

# print("")
# x = [0.2,0.3]
# y = [-0.28398668,0.00660095]
# print("points interpolated:", x, y)
# polynomial = interpolating_polynomial(x,y)
# print("Polynomial:", polynomial)

# # Evaluate the polynomial at x = 2
# value_at_p = evaluate_polynomial(polynomial, 0.25)
# print("Value at x=0.25:", value_at_p)

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)




def newtons_forward_differences(x_samples, y_samples):
    n = len(x_samples)
    divided_differences = []
    divided_differences.append(y_samples)
    difference_num = 1
    while True :
        new_row = []
        for i in range(len(divided_differences[-1])-1):
            new_row.append(divided_differences[-1][i+1] - divided_differences[-1][i])
        divided_differences.append(new_row)
        difference_num += 1
        if len(new_row) == 1:
            break
    return divided_differences



def newton_forward_interpolating_polynomial(x_samples, y_samples):
    h = x_samples[1]-x_samples[0]
    n = len(x_samples)
    divided_differences = newtons_forward_differences(x_samples, y_samples)
    polynomial = ""
    for i in range(n):
        if divided_differences[i][0]!=0:
            value = (divided_differences[i][0]/fact(i))/(h**i)
            polynomial += str(value)
            for j in range(i):
                polynomial += "*(x - " + str(x_samples[j]) + ")"
            if i != n-1:
                polynomial += " + "
    polynomial += "+ 0"
    return polynomial

print(newton_forward_interpolating_polynomial([1,2,3,4],[1,4,9,16]))


# Example usage
x = [-0.75,-0.5,-0.25,0]
y = [-0.07181250,-0.02475,0.3349375,1.101000]
print("points interpolated:", x, y)
polynomial = newton_forward_interpolating_polynomial(x,y)
print("Polynomial:", polynomial)

# Evaluate the polynomial at x = 2
value_at_p = evaluate_polynomial(polynomial, -1/3)
print("Value at x=-1/3:", value_at_p)

# x = [-0.75,0]
# y = [-0.07181250,1.101000]
# print("points interpolated:", x, y)
# polynomial = newton_forward_interpolating_polynomial(x,y)
# print("Polynomial:", polynomial)

# # Evaluate the polynomial at x = 2
# value_at_p = evaluate_polynomial(polynomial, -1/3)
# print("Value at x=-1/3:", value_at_p)

# le usage
x = [-0.75,-0.5]
y = [-0.07181250,-0.02475]
print("points interpolated:", x, y)
polynomial = newton_forward_interpolating_polynomial(x,y)
print("Polynomial:", polynomial)

# Evaluate the polynomial at x = 2
value_at_p = evaluate_polynomial(polynomial, -1/3)
print("Value at x=-1/3:", value_at_p)



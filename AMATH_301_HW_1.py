import numpy as np

# Question 1

A = np.array([[1.0, -2.3], [4.5, np.e ** 2]])
B = np.array([[6, 2, 4, -3], [np.pi, 9, 3.6, -2.1]])
C = np.array([[3.7, -2.4, 0], [4, 1.8, -11.6], [2.3, -3.3, 5.9]])

x = np.array([[5], [np.sin(4)], [-3]])
y = np.array([[8, -6]])
z = np.array([[3], [0], [np.tan(2)], [-4.7]])

A1 = 3*x
A2 = np.matmul(z.transpose(), B.transpose()) + y
A3 = np.matmul(C, x)
A4 = np.matmul(A, B)
A5 = np.matmul(B.transpose(), A.transpose())

# Question 2

x = np.zeros((73))
for i in range(73):
    x[i] = (-4. + i * (5. / 72.))
y = np.zeros((73))
for i in range(73):
    y[i] = np.cos(i)

A6 = x
A7 = y
A8 = x * y
A9 = x / y
A10 = x ** 3 - y

# Question 3

A11 = 0.
A12 = 0.
A13 = 1
A14 = 0.
A15 = 1
A16 = 0.

for i in range(1, 11):
    A11 += 1. / i
for i in range(1, 101):
    A12 += 1. / i
while A14 < 5:
    A14 += 1. / A13
    A13 += 1
while A16 < 15:
    A16 += 1. / A15
    A15 += 1

A13 -= 1
A15 -= 1

# Question 4

A17 = np.array([[2, -1, 0], [-1, 3, -1], [0, -1, 2]])
A18 = np.array([5, 0, 6])
A19 = np.linalg.solve(A17, A18)
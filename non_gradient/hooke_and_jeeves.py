import numpy as np


def J(x):
    return ((x[0]-2)^4) + (x[0] - 2*x[1])^2


k = 1
n = 2
F = 2

eps = 0.09

d = np.identity(2)
D = np.array([[0.2,0.2]]).T

x_initial = np.array([[2,3]]).T 

x = list()
y = list()

print('Funcion objetivo')
print(J(x_initial))
# while (D[0] + D[1]/2) > eps:
#     pass
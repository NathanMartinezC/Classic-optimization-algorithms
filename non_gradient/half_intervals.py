import numpy as np
import pandas as pd 

#Objective function definition
def J(x):
    func = np.power(x,2) + 2*x
    return func

iter_num = 15 #Iteations number
eps = 0.001 

#Vector initialization
a = np.zeros(iter_num)
b = np.zeros(iter_num)
L = np.zeros(iter_num)
fb = np.zeros(iter_num)
fa = np.zeros(iter_num)
alp = np.zeros(iter_num)
lam = np.zeros(iter_num)
mu = np.zeros(iter_num)
f_alp = np.zeros(iter_num)
f_lam = np.zeros(iter_num)
f_mu = np.zeros(iter_num)
i = np.arange(iter_num)

#Setting initial values
a[0] = -3
b[0] = 6
L[0] = b[0] - a[0]
fb[0] = J(b[0])
fa[0] = J(a[0])
alp[0] = (a[0] + b[0])/2

for k in range(iter_num-1):
    lam[k] = a[k] + L[k]/4
    mu[k] = b[k] - L[k]/4
    f_alp[k] = J(alp[k])
    f_lam[k] = J(lam[k])
    f_mu[k] = J(mu[k])

    if f_lam[k] < f_alp[k]:
        b[k+1] = alp[k]
        alp[k+1] = lam[k]
        a[k+1] = a[k]
       
    elif f_mu[k] < f_alp[k]:
        a[k+1] = alp[k]
        alp[k+1] = mu[k]
        b[k+1] = b[k]

    else:
        a[k+1] = lam[k]
        b[k+1] = mu[k]
        alp[k+1] = alp[k]
    
    L[k+1] = b[k+1] - a[k+1]
    
data = np.array([a, b, L, alp]).T
columns = ["ak", "bk", "xk", "Lk"]
results = pd.DataFrame(data=data, columns=columns)
print(results)
print(f"Optimum: {alp[-1]}")
        

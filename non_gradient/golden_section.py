import numpy as np 
import pandas as pd 

#Objective function definition
def J(x):
    func = np.power(x,2) + 2*x
    return func

#Value initialization
a_init = -3
b_init = 6
eps = 0.001
tau = (np.sqrt(5) - 1)/2
iter_num = int(1 + (np.log(eps) - np.log(b_init - a_init))/np.log(tau))
# lam_init = a_init + (1-tau)*(b_init - a_init)
# mu_init = a_init + tau*(b_init -a_init)

#Vector initialization
a = np.zeros(iter_num)
b = np.zeros(iter_num)
lam = np.zeros(iter_num)
mu = np.zeros(iter_num)
f_lam = np.zeros(iter_num)
f_mu = np.zeros(iter_num)
L = np.zeros(iter_num)

a[0] = a_init
b[0] = b_init
lam[0] = a_init + (1-tau)*(b_init - a_init)
mu[0] = a_init + tau*(b_init -a_init)

for k in range(iter_num - 1):
    f_lam[k] = J(lam[k])
    f_mu[k] = J(mu[k])

    if f_lam[k] > f_mu[k]:
        a[k+1] = lam[k]
        b[k+1] = b[k]
        lam[k+1] = mu[k]
        mu[k+1] = a[k+1] + tau*(b[k+1] - a[k+1])
    else:
        a[k+1] = a[k]
        b[k+1] = mu[k]
        mu[k+1] = lam[k]
        lam[k+1] = a[k+1] + (1 - tau)*(b[k+1] - a[k+1])

    L[k] = b[k] - a[k]

data = np.array([a, b, L, lam]).T
columns = ["ak", "bk", "xk", "Lk"]
results = pd.DataFrame(data=data, columns=columns)
print(results)
print(f"Optimum: {lam[-1]}")





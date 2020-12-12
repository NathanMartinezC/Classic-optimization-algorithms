import numpy as np 
import pandas as pd

def J(x):
    func = np.power(x,2) + 2*x
    return func

def fibonacci(x):
    f = np.zeros(x)
    for i in range(x):
        if i==0 or i==1:
            f[i] = 1
        else:
            f[i] = f[i-1] + f[i-2]
    return f

#Value initialization
eps = 0.001
n = 21
F = fibonacci(n)
a_init = -3
b_init = 6
k = 2

#Vector initialization
a = np.zeros(n)
b = np.zeros(n)
lam = np.zeros(n)
mu = np.zeros(n)
f_lam = np.zeros(n)
f_mu = np.zeros(n)
L = np.zeros(n)
th_lam = np.zeros(n)
th_mu = np.zeros(n)

n = n-1

a[0] = a_init
b[0] = b_init
lam[0] = a_init + (F[n-2]/F[n])*(b[0] - a[0])
mu[0] = a_init + (F[n-1]/F[n])*(b[0] - a[0])


for k in range(n):
    th_lam[k] = J(lam[k])
    th_mu[k] = J(mu[k])

    if th_lam[k] > th_mu[k]:
        a[k+1] = lam[k]
        b[k+1] = b[k]
        lam[k+1] = mu[k]
        mu[k+1] = a[k+1] + (F[n-k-1]/F[n-k])*(b[k+1] - a[k+1])

        if k == n-2:
            lam[k] = lam[k-1]
            mu[k] = lam[k-1] + eps
            th_lam[k] = J(lam[k])
            th_mu[k] = J(mu[k])
            if th_lam[k] > th_mu[k]:
                a[k] = lam[k]
                b[k] = b[k-1]
            else:
                a[k] = a[k-1]
                b[k] = lam[k]
        else:
            th_mu[k+1] = J(mu[k+1])

    else:
        a[k+1] = a[k]
        b[k+1] = mu[k]
        mu[k+1] = lam[k]
        lam[k+1] = a[k+1] + (F[n-k-2]/F[n-k])*(b[k+1] - a[k+1])

        if k == n-2:
            lam[k] = lam[k-1]
            mu[k] = lam[k-1] + eps
            th_lam[k] = J(lam[k])
            th_mu[k] = J(mu[k])
            if th_lam[k] > th_mu[k]:
                a[k] = lam[k]
                b[k] = b[k-1]
            else:
                a[k] = a[k-1]
                b[k] = lam[k]
        else:
            th_lam[k+1] = J(lam[k+1])


optimum = a[-1] + 0.5*(b[-1] - a[-1])

data = np.array([a, b, lam, mu, th_lam, th_mu]).T
columns = ["ak", "bk", "lam", "mu", "th_lam", "th_mu"]
results = pd.DataFrame(data=data, columns=columns)
print(results)

print(f"Optimum: {optimum}")

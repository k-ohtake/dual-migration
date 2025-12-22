# -*- coding: utf-8 -*-
"""
Paper: City formation by dual migration of firms and workers
Author: Kensuke Ohtake
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
plt.rcdefaults()
sns.set(style='darkgrid')

# hyper parameters
mu = 0.6 # mu
sig = 5.0 # sigma
vn = 1.0 # realprofit sensitivity of firms
vm = 1.0 # realwage sensitivity of workers
r = 1.0 # radius of S

# transport coefficient
tau = np.linspace(0.001, 8, 256) # tau
alp = tau * (sig - 1.0) # alpha

# loop in frequency numbers
for n in [1, 2, 3, 4, 5, 6]: # list of frequency number
    
    # compute Z_k: transport index
    if n % 2 == 0:# for even frequency
        Z = (
            (np.power(alp, 2.0) * np.power(r, 2.0))
            / (np.power(float(n), 2.0) + np.power(alp, 2.0) * np.power(r, 2.0))
            )
    else: # for odd frequency
        Z = (
            (np.power(alp, 2.0) * np.power(r, 2.0) 
             * (1.0 + np.exp(- alp * r * np.pi))) 
            / ((np.power(float(n), 2.0) + np.power(alp, 2.0) * np.power(r, 2.0))
               * (1.0 - np.exp(- alp * r * np.pi)))
            )
    
    # determinat of linear operator
    det = 1.0 - (mu / sig) * Z - ((sig - 1.0) / sig) * np.power(Z, 2.0)
    
    # compute discriminant of the characteristic polynomial
    A = (
        (1.0 
         + (mu / (sig - 1.0)) * Z 
         - (1.0 + (np.power(mu, 2.0) / (sig - 1.0)))
         * np.power(Z, 2.0)) / det
        )
    B = - np.power(mu * Z - 1.0, 2.0) / det
    b = (
        - (vn * mu * ((A / sig) - 1.0)
           + vm * B)
        ) # b in quadratic polynomial
    c = - vn * vm * mu * (A + B) # c in quadratic polynomial
    D = np.power(b, 2.0) - 4.0 * c # discriminant
    
    # If it has complex solutions then stop
    if np.any(D < 0) == True:
        print("D < 0")
        sys.exit()
    else:
        pass
    
    # larger eigenvalue
    larger_ev = (- b + np.sqrt(D)) / 2.0
    
    # smaller eigenvalue
    # smaller_ev = (-b - np.sqrt(D)) / 2.0
    
    # plot larger eigenvalue
    plt.plot(tau, larger_ev, linewidth=2, label=r"$k={}$".format(int(n)))

# plot centerline
zr = np.zeros(len(tau))
plt.plot(tau, zr, color="black", linewidth=0.5, linestyle="dashed") # center line

# plot critical points
plt.plot(0.9149602289091033, 0, 'o', markersize=1, color="black")
plt.text(1, 0, r"$\tau_1^*$", ha="center", va="bottom", fontsize=10)

plt.plot(1.8301475162541556, 0, 'o', markersize=1, color="black")
plt.text(2, 0, r"$\tau_2^*$", ha="center", va="bottom", fontsize=10)

plt.plot(2.745221274381233, 0, 'o', markersize=1, color="black")
plt.text(3, 0, r"$\tau_3^*$", ha="center", va="bottom", fontsize=10)

plt.plot(3.6602950325083112, 0, 'o', markersize=1, color="black")
plt.text(4, 0, r"$\tau_4^*$", ha="center", va="bottom", fontsize=10)

plt.plot(4.575368790635389, 0, 'o', markersize=1, color="black")
plt.text(4.8, 0, r"$\tau_5^*$", ha="center", va="bottom", fontsize=10)

plt.plot(5.490442548762466, 0, 'o', markersize=1, color="black")
plt.text(5.8, 0, r"$\tau_6^*$", ha="center", va="bottom", fontsize=10)

# labels
plt.xlabel(r"$\tau$")
plt.ylabel("maximal real part of eigenvalues")

# legends
plt.legend(fontsize=8, loc="upper right")
plt.savefig("eigens.png", format="png", dpi=300)

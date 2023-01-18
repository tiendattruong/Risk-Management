#C-Exercise 15
#Tien Dat Truong
#stu213245

import scipy.stats
import math
import numpy as np
import matplotlib.pyplot as plt

#a
def GARCH11_MC(n, m, theta, sigma1):
    X = np.zeros((m,n))
    sigma_sq= np.ones((m,n))*sigma1**2
    for i in range(0, m):
        Y = np.random.normal(0, 1, n)
        sigma_sq[i,1:] = theta(0)+theta(1)*X[i, :]**2+theta(2)*sigma_sq[i, :]
        X[i, :] = Y[i, :]*np.sqrt(sigma_sq[i, :])
    return (X,sigma_sq)
#b
def VaR_ES_GARCH11_MC(k, m, l, alpha, theta, sigma1):


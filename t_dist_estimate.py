#C-Exercise 23
#Tien Dat Truong
#stu213245


import math
import numpy as np
import matplotlib.pyplot as plt


# function for estimation of t-distribution
def t_dist_estimate(x_data):
    # number of observations
    n = len(x_data)

    # estimators for mean vector and covariance matrix
    mu_hat = np.mean(x_data, axis=0)
    d = len(mu_hat)
    C_hat = np.cov(x_data.T)
    C_inv = np.linalg.inv(C_hat)
    det_C = np.linalg.det(C_hat)
    factor1 = 1 / math.sqrt(det_C)

    # log-likelihood function w.r.t. nu
    def ll(nu):
        v = np.zeros(len(nu) + 1)
        for i in range(0, len(nu)):
            v1 = 0
            nu_it = nu[i]
            factor2 = math.gamma(0.5 * (nu_it + d)) / math.gamma(0.5 * nu_it) / (math.pi * (nu_it - 2)) ** (0.5 * d)
            expo = -0.5 * (nu_it + d)
            factor3 = 1 / (nu_it - 2)
            for k in range(0, n):
                x_it = x_data[k, :]
                v1 += math.log(
                    factor2 * factor1 * (1 + factor3 * np.dot(x_it - mu_hat, np.dot(C_inv, x_it - mu_hat))) ** expo)
            v[i] = v1
        return v

    test = np.linspace(2.1, 5, 30)
    ind = np.argmin(-ll(test))
    nu_hat = test[ind]

    Sigma_hat = (nu_hat - 2) / nu_hat * C_hat

    return nu_hat, mu_hat, Sigma_hat


# part a)
def t_dist_MC_sim(n, nu, mu, Sigma):

    return x


# part b)
def VaR_ES_historic_mult(x_data, l, alpha):
    return VaR, ES


def VaR_ES_t_dist_MC(x_data, l, alpha, N):
    return VaR, ES


# part c)
# trading days
td = 252

# level alpha
alpha = 0.97

# number of Monte-Carlo simulations
N = 2000

# import timeseries
n = 5369  # number of trading days
S = np.zeros((2, n))
i = 0
for file in ['BMW.csv', 'Continental.csv']:
    with open(file) as csv:
        # change decimal from comma to point
        S[i] = np.flip(np.genfromtxt((line.replace(',', '.') for line in csv), delimiter=';', skip_header=1, usecols=4))
    i += 1

# log returns

# memory for estimates

# compute initial portfolio

# estimation for each trading day i>=td+2
    
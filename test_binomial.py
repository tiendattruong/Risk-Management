#C-Exercise 07
#Tien Dat Truong
#stu213245

import scipy.stats
import math
import numpy as np
import matplotlib.pyplot as plt

#Create function
def test_binomial(v,p0,alpha):
    n=len(v)
    test= scipy.stats.binom_test(p*n,n,p,alternative="two-sided")
    if test > scipy.stats.t.ppf(1-alpha/2,n):
        result=1
    else:
        result = 0
    return result

#Input data from exercise 05
def VaR_log_normal(s,alpha):
    X= np.diff(np.log(s))
    ev=np.mean(X)
    std_dev= np.sqrt(np.var(X))
    VaR = s[251]*(1-np.exp(ev+std_dev*scipy.stats.norm.ppf(1-alpha)))
    return VaR
dax = np.genfromtxt('dax_data.csv', delimiter=';', usecols=4, skip_header=1)
dax=np.flip(dax)
n=len(dax)
s=np.zeros((n-252,252))
for i in range (0,n-252,1):
    for j in range (0,252,1):
        s[i,j] = dax[i+j+1]
VaR1= np.zeros(n-252)
VaR2= np.zeros(n-252)
for i in range(0,n-252):
    VaR1[i]= VaR_log_normal(s[i],0.9)
    VaR2[i]= VaR_log_normal(s[i],0.95)
X= np.diff(np.log(dax))
L=np.zeros(n-252)
for i in range (0,n-253):
    L[i]=-dax[i+251]*(dax[i+252]/dax[i+251]-1)

#Test Function
Violation=VaR2+L
p=len([1 for i in Violation if i < 0])/len(Violation)
test=test_binomial(Violation,p,0.05)
print(test)




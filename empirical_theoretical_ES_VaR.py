#C-Exercise 13
#Tien Dat Truong
#stu213245

import scipy.stats
import math
import numpy as np
import matplotlib.pyplot as plt

#a
def empirical_cdf(n):
    z=np.random.normal(0,1,n)
    x= np.sort(np.random.normal(0,1,n))
    n= x.size
    y = np.arange(1,n+1)/n
    return (x,y,z)

ecdf_10= empirical_cdf(10)
ecdf_100= empirical_cdf(100)
ecdf_1000= empirical_cdf(1000)
cdf_10 = scipy.stats.norm.cdf(ecdf_10[0])
cdf_100 = scipy.stats.norm.cdf(ecdf_100[0])
cdf_1000 = scipy.stats.norm.cdf(ecdf_1000[0])

plt.clf()
plt.subplot(3,1,1)
plt.plot(ecdf_10[0],ecdf_10[1])
plt.plot(ecdf_10[0],cdf_10)
plt.subplot(3,1,2)
plt.plot(ecdf_100[0],ecdf_100[1])
plt.plot(ecdf_100[0],cdf_100)
plt.subplot(3,1,3)
plt.plot(ecdf_1000[0],ecdf_1000[1])
plt.plot(ecdf_1000[0],cdf_1000)
plt.show()
#b

def empirical_ES_VaR(sample,alpha):
    loss=np.diff(sample)
    n=len(loss)
    a=np.floor(n*alpha+1)
    ES= 1/a*np.sum(sample[0:int(a)-1])
    VaR= np.sum(sample[0:int(a)-1])
    return (ES,VaR)

def theoretical_ES_VaR(sample,alpha):
    mu=np.mean(sample)
    sigma=np.sqrt(np.var(sample))
    ES= mu+sigma*scipy.stats.norm.cdf(scipy.stats.norm.ppf(1-alpha))/alpha
    VaR= mu+sigma*scipy.stats.norm.ppf(1-alpha)
    return (ES,VaR)

alpha=(0.1,0.025)

#n=10
A=empirical_ES_VaR(ecdf_10[2],alpha[0])
B=empirical_ES_VaR(ecdf_10[2],alpha[1])
C=theoretical_ES_VaR(ecdf_10[2],alpha[0])
D=theoretical_ES_VaR(ecdf_10[2],alpha[1])
print(A,C)
print(B,D)
#n=100
E=empirical_ES_VaR(ecdf_100[2],alpha[0])
F=empirical_ES_VaR(ecdf_100[2],alpha[1])
G=theoretical_ES_VaR(ecdf_100[2],alpha[0])
H=theoretical_ES_VaR(ecdf_100[2],alpha[1])
print(E,G)
print(F,H)
#n=1000
I=empirical_ES_VaR(ecdf_1000[2],alpha[0])
J=empirical_ES_VaR(ecdf_1000[2],alpha[1])
K=theoretical_ES_VaR(ecdf_1000[2],alpha[0])
L=theoretical_ES_VaR(ecdf_1000[2],alpha[1])
print(I,K)
print(J,L)





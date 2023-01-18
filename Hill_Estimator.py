#C-Exercise 19
#Tien Dat Truong
#stu213245

import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt

#a
def Hill_Estimator(x,k):
    x_sort=np.sort(x)
    lower= np.zeros(k-1)
    for i in range (0,k-2):
        lower[i]=np.log(x_sort[i]/x_sort[k-1])
    result= k/np.sum(lower)
    return result
#b
def Hill_Plot(x):
    n= len(x)
    k=list(range(2,n+1))
    alpha=np.zeros(len(k))
    for i in range(0,len(k)-1):
        alpha[i]= Hill_Estimator(x,k[i])
    result=plt.scatter(k,alpha)
    return result
#C
ref_1= np.random.standard_t(3,500)
ref_2= np.random.standard_t(8,500)
ref_3 = np.random.exponential(1,500)
a= Hill_Plot(ref_1)
b= Hill_Plot(ref_2)
c= Hill_Plot(ref_3)
plt.show()
#d
def VaR_ES_Hill(x, p, k):
    x_sort = np.sort(x)
    n=len(x)
    alpha= Hill_Estimator(x,k)
    VaR= (((n/k)*(1-p))**(-1/alpha))*x_sort[k-1]
    ES= ((1-1/alpha)**(-1))*VaR
    return (VaR,ES)
#e
data = np.genfromtxt('RiskMan_2020_Exercise_19_data.dat')
data=np.flip(data)
result= VaR_ES_Hill(data,0.98,100)
print(result)
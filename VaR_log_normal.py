#C-Exercise 05
#Tien Dat Truong
#stu213245

import scipy.stats
import math
import numpy as np
import matplotlib.pyplot as plt

#a Create a function
def VaR_log_normal(s,alpha):
    X= np.diff(np.log(s))
    ev=np.mean(X)
    std_dev= np.sqrt(np.var(X))
    VaR = s[251]*(1-np.exp(ev+std_dev*scipy.stats.norm.ppf(1-alpha)))
    return VaR
# Import data
dax = np.genfromtxt('dax_data.csv', delimiter=';', usecols=4, skip_header=1)
dax=np.flip(dax)
n=len(dax)
# Create price matrix for function
s=np.zeros((n-252,252))
for i in range (0,n-252,1):
    for j in range (0,252,1):
        s[i,j] = dax[i+j+1]
# Using function
VaR1= np.zeros(n-252)
VaR2= np.zeros(n-252)
for i in range(0,n-252):
    VaR1[i]= VaR_log_normal(s[i],0.9)
    VaR2[i]= VaR_log_normal(s[i],0.95)
X= np.diff(np.log(dax))
L=np.zeros(n-252)
for i in range (0,n-253):
    L[i]=-dax[i+251]*(dax[i+252]/dax[i+251]-1)
#Plotting
plt.subplot(2,1,1)
plt.plot(VaR1+L,'r')
plt.subplot(2,1,2)
plt.plot(VaR2+L, 'b')
plt.show()
#Percent that actual loss lie above computed var(sum is under 0)
#90%
a=VaR1+L
b=len([1 for i in a if i < 0])
print(b*100/len(L),'%')
#95%
c=VaR2+L
d=len([1 for i in c if i < 0])
print(b*100/len(L),'%')
#Theoretically, I expected it under 30%. However, the result is unexpected high, under 10%
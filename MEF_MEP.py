#C-Exercise 27
#Tien Dat Truong
#stu213245

import numpy as np
import matplotlib.pyplot as plt

#a
def MEF(x,u):
    a=np.zeros(len(x))
    for i in range (0,len(x)-1):
        if x[i]>u:
            a[i]=x[i]-u
        else:
            a[i]=0
    n= len([i for i in a if i > 0])
    if n==0:
        mean=0
    else:
        mean= sum(a)/n
    return mean
#b
def MEP(x):
    n=len(x)
    x_hat = x[1:n-1]
    mean= np.zeros(len(x_hat))
    for i in range (1, n-1):
        x_2=x[0:i]
        mean[i-1]=MEF(x_2,x[i])
    plot= plt.scatter(x_hat,mean)
    return plot
#C
sample_1 = np.random.standard_t(3,500)
sample_2 = np.random.standard_t(8,500)
sample_3 = np.random.exponential(1,500)
plot1=MEP(sample_1)
plt.show()
plot2=MEP(sample_2)
plt.show()
plot3=MEP(sample_3)
plt.show()

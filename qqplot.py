#C-Exercise 18
#Tien Dat Truong
#stu213245

import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt

#a
def qqplot(x, F_inv):
    x_hat=np.sort(x)
    result=plt.scatter(x_hat,F_inv)
    return result

#b
bmw = np.genfromtxt('bmw.csv', delimiter=';', usecols=4, skip_header=1)
bmw = np.diff(np.log(np.flip(bmw)))

ref1=np.sort(np.random.normal(0,1,len(bmw)))
ref2=np.sort(np.random.standard_t(10,len(bmw)))
ref3=np.sort(np.random.standard_t(5,len(bmw)))
a=qqplot(bmw,ref1)
b=qqplot(bmw,ref2)
b=qqplot(bmw,ref3)
plt.show()


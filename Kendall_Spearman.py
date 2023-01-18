#C-Exercise 21
#Tien Dat Truong
#stu213245

import numpy as np
from scipy import stats
from scipy import special
import matplotlib.pyplot as plt

#a
def Kendall(x):
    (tau,p_value)=stats.kendalltau(x[0],x[1])
    return tau
#b
def Spearman(x):
    (rho,p_value)=stats.spearmanr(x[0],x[1])
    return rho
#c
continential = np.genfromtxt('continential.csv', delimiter=';', usecols=4, skip_header=1)
continential=np.diff(np.log(np.flip(continential)))
vw = np.genfromtxt('vw.csv', delimiter=';', usecols=4, skip_header=1)
vw=np.diff(np.log(np.flip(vw)))
x=(vw,continential)

a=np.corrcoef(x[0],x[1])
b= Kendall(x)
c= Spearman(x)
print(a[0,1],b,c)
#d
mean=(np.mean(x[0]),np.mean(x[1]))
cov_matrix= np.cov(x[0],x[1])
sample=np.random.multivariate_normal(mean,cov_matrix,5369).T
tau=Kendall(sample)
rho=Spearman(sample)
print(tau,rho)
plt.clf()
plt.scatter(sample[0],sample[1])
plt.show()
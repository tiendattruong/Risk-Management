#C-Exercise 09
#Tien Dat Truong
#stu213245

import scipy.stats
import math
import numpy as np
import matplotlib.pyplot as plt

#a.Creating a function
def VaR_ES_var_covar (x_data, c, w, alpha):
    n=len(x_data)
    ll= np.zeros(n)
    for i in range (0,n-1,1):
        ll[i]= -(c+w[i]*x_data[i])
    mean=np.mean(x_data)
    var= np.var(x_data)
    VaR= -(c+w*mean)+np.sqrt(var)*scipy.stats.norm.ppf(alpha)
    ES= -(c+w*mean) +np.sqrt(var)*(scipy.stats.norm.cdf(scipy.stats.norm.ppf(alpha)))/(1-alpha)
    return (VaR,ES)
#b. Input data and compute log return
bmw = np.genfromtxt('bmw.csv', delimiter=';', usecols=4, skip_header=1)
bmw = np.diff(np.log(np.flip(bmw)))
sap = np.genfromtxt('sap.csv', delimiter=';', usecols=4, skip_header=1)
sap =np.diff(np.log(np.flip(sap)))
siemens = np.genfromtxt('siemens.csv', delimiter=';', usecols=4, skip_header=1)
siemens=np.diff(np.log(np.flip(siemens)))
continential = np.genfromtxt('continential.csv', delimiter=';', usecols=4, skip_header=1)
continential=np.diff(np.log(np.flip(continential)))
vw = np.genfromtxt('vw.csv', delimiter=';', usecols=4, skip_header=1)
vw=np.diff(np.log(np.flip(vw)))
data=(bmw,continential,sap,siemens,vw)
print(data)
#c

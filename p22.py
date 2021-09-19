#Principal Component Analysis
#Sample Covariance Matrix
#Population Covariance Matrix

import numpy as np

data_set=np.array([
    [1,2],
    [1,1.2],
    [2.3,5.4],
    [4,9],
    [1.5,7],
    [8.7,2.1],
    [1.8,4.5]
])

#Number of data points = N
#Number of Dimensions = D

N,D=np.shape(data_set)

print("Number of Data points is ", N, " and number of dimensions is ", D)

#Population Covariance Matrix
P=np.cov(np.transpose(data_set), bias=True)
print("Population Covariance Matrix:")
print(P)

#Sample Covariance Matrix
S=np.cov(np.transpose(data_set), bias=False)
print("Sample Covariance Matrix:")
print(S)

#We are taking the transform before finding the covariance matrix because the np.cov function expects data in column format
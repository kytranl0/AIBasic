from sklearn import preprocessing
import numpy as np 

'''
Standard Scalar

(Xi - Xmean) / (std of feature(all elements in array,list))

'''

x = np.array([[-400], [-100], [0], [100], [400]])
x1 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
standardscaler = preprocessing.StandardScaler()
x_scaler = standardscaler.fit_transform(x)
x_scaler1 = standardscaler.fit_transform(x1)

print(x_scaler)
print(x_scaler1)
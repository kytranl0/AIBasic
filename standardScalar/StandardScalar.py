from sklearn import preprocessing
import numpy as np 

'''
Standard Scalar

(Xi - Xmean) / (std of feature(all elements in array,list))
'''

x = np.array([[-400], [-100], [0], [100], [400]])

standardscaler = preprocessing.StandardScaler()
x_scaler = standardscaler.fit_transform(x)

print(x_scaler)
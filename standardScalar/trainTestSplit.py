import numpy as np
from sklearn.model_selection import train_test_split
x = np.arange(1, 25).reshape(12, 2)
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
x_train, x_test, y_train, y_test = train_test_split(x, y)
print(x_train)
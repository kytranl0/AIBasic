import numpy as np
from sklearn.model_selection import train_test_split
x = np.arange(1, 25).reshape(12, 2)
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
x_train, x_test, y_train, y_test = train_test_split(x, y)
print("x")
print(x)

print("y")
print(y)

print("x_train")
print(x_train)

# Splitting a dataset might also be important for detecting if your model suffers from one of two very common problems, called underfitting and overfitting:
# Underfitting is usually the consequence of a model being unable to encapsulate the relations among data. For example, this can happen when trying to represent nonlinear relations with a linear model. Underfitted models will likely have poor performance with both training and test sets.
# Overfitting usually takes place when a model has an excessively complex structure and learns both the existing relations among data and noise. Such models often have bad generalization capabilities. Although they work well with training data, they usually yield poor performance with unseen (test) data.
print("x_test")

print(x_test)

print("y_train")
print(y_train)


print("y_test")
print(y_test)


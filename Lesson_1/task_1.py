import numpy as np


x = 1
y = np.log(np.exp(1 / (np.sin(x) + 1))) / ((5 / 4) + (1 / x**15)) / np.log(1 + x**2)


print (y)
x = 10
y = np.log(np.exp(1 / (np.sin(x) + 1))) / ((5 / 4) + (1 / x**15)) / np.log(1 + x**2)
print (y)
x = 1000
y = np.log(np.exp(1 / (np.sin(x) + 1))) / ((5 / 4) + (1 / x**15)) / np.log(1 + x**2)
print (y)

input("")
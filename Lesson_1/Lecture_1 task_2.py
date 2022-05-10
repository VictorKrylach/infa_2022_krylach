#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1.1, 0.1)
plt.plot(x, x**x - x - 6)
plt.grid(True)
plt.show()



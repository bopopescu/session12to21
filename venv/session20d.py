import numpy as nm
import matplotlib.pyplot as plt

x=nm.random.randn(50)
print(x)

plt.hist(x,100)
plt.show()

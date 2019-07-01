import numpy as np
import time

stamp1 = time.time()

arr1 = np.array([10, 20, 30, 40, 50])
a2 = np.array([[10, 20, 30, 40], [40, 50, 60, 40], [70, 80, 90, 40]])

a3 = a2.ravel()
print(a3)

stamp2 = time.time()

print("Difference:",stamp2-stamp1)
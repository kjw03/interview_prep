import time

import numpy as np


a = [2, 4, 5, 3, 7, 8, 9, 12, 45, 23,
              45, 23, 43, 23, 43, 23, 12, 239, 54, 854, 34, 23,
              45, 23, 433, 23, 43, 2, 12, 239, 54, 854, 34, 23,
              45, 23, 43, 29, 43, 25, 12, 239, 54, 854, 34, 23]

b = [2, 34, 45, 53, 67, 38, 19, 212, 45, 23, 
              45, 23, 43, 23, 43, 23, 12, 94, 3, 85, 34, 12,
              45, 23, 43, 23, 43, 23, 12, 94, 3, 85, 34, 12,
              45, 23, 43, 23, 3, 23, 12, 9, 3, 85, 3, 12]

a_np = np.array(a)
b_np = np.array(b)

iterations = 10000

tic = time.perf_counter()
run_sum = 0
for i in range(iterations):
    for j in range(len(a)):
        run_sum += a[j] * b[j]
toc = time.perf_counter()
print(f"{iterations} iterations without numpy vectorization {toc - tic:0.4f} seconds")



tic = time.perf_counter()
for i in range(iterations):
    sum = np.dot(a_np, b_np)
toc = time.perf_counter()
print(f"{iterations} iterations with numpy vectorization {toc - tic:0.4f} seconds")
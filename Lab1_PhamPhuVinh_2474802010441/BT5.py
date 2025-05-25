import numpy as np
from sympy import Symbol, solve
M1 = np.array([[9, 12], [23, 30]])
print("Bài 5 - Ma trận M1:\n", M1)
u = np.array([2, 1])
tichM1u = M1.dot(u)
print("Bài 5 - M1 nhân u:", tichM1u)  # [30 76]
tichuM1 = u.dot(M1)
print("Bài 5 - u nhân M1:", tichuM1)  # [41 54]
print("Bài 5 - np.dot(M1, u):", np.dot(M1, u))  # [30 76]
print("Bài 5 - np.dot(u, M1):", np.dot(u, M1))  # [41 54]

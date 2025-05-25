import numpy as np
from sympy import Symbol, solve
x = Symbol('x')
ptb2 = x**2 + 9*x + 8
print("Bài 2 - Nghiệm pt x^2 + 9x + 8 = 0:", solve(ptb2, dict=True))  
# [{x: -8}, {x: -1}]
ptb2 = x**2 + x + 10
nghiemx = solve(ptb2, dict=True)
print("Bài 2 - Nghiệm pt x^2 + x + 10 = 0:", nghiemx)  
# Nghiệm phức
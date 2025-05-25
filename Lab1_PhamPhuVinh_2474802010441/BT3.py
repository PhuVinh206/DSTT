from sympy import Symbol, solve
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
ptb2 = a*x**2 + b*x + c
nghiem = solve(ptb2, x, dict=True)
print("Bài 3 - Nghiệm tổng quát ax^2 + bx + c = 0:", nghiem)
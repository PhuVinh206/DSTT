from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5
nghiem = solve((pt1, pt2), dict=True)
print("Bài 4 - Nghiệm hệ phương trình:", nghiem)
nghiem = nghiem[0]
print("Bài 4 - Thay nghiệm vào pt1:", pt1.subs({x: nghiem[x], y: nghiem[y]}))
print("Bài 4 - Thay nghiệm vào pt2:", pt2.subs({x: nghiem[x], y: nghiem[y]}))
from sympy import Symbol, solve
x = Symbol('x')
bieuthuc = x + 3 - 5
print("Bài 1 - Nghiệm phương trình x + 3 = 5:", solve(bieuthuc))  
# [2]
bieuthuc = x**2 + 3 - 5
nghiemx = solve(bieuthuc)
print("Bài 1 - Nghiệm phương trình x^2 + 3 = 5:", nghiemx)        
# [-√2, √2]
print("Bài 1 - Nghiệm 1:", nghiemx[0])                            
# -√2
print("Bài 1 - Nghiệm 2:", nghiemx[1])                            
# √2
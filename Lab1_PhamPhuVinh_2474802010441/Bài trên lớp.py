danhsach1 = [1. , 3.] 
danhsach2 = [5. , 7.] 
danhsach = danhsach1 + danhsach2 
print("Kết quả của danh sách sau khi cộng:", danhsach)
#Kết quả của danh sách sau khi cộng: [1.0, 3.0, 5.0, 7.0]

danhsach_gapdoi = 2 * danhsach
#Kết quả của danh sách [1, 3, 5, 7] * 2 = [1, 3, 5, 7, 1, 3, 5, 7]

danhsach * 2
# Kết quả của danh sách [1, 3, 5, 7, 1, 3, 5, 7]

danhsach / 2
# TypeError (không hợp lệ)

mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
anh_xa_list = list(anh_xa)
print("Kết quả zip (anh_xa):")
print(anh_xa_list)
tap_hop = set(anh_xa_list)
print("Tập hợp tap_hop:")
print(tap_hop)
lay_TT, lay_monhoc, lay_diem = zip(*tap_hop)
print("Danh sách thứ tự:", lay_TT)
print("Danh sách môn học:", lay_monhoc)
print("Danh sách điểm:", lay_diem)
#Kết quả zip (anh_xa):
#[(2, 'ToanCC', 10), (3, 'DSTT', 9), (4, 'ToanRR', 8), (1, 'LaptrinhCB', 7)]
#Tập hợp tap_hop:
#{(3, 'DSTT', 9), (4, 'ToanRR', 8), (1, 'LaptrinhCB', 7), (2, 'ToanCC', 10)}
#Danh sách thứ tự: (3, 4, 1, 2)
#Danh sách môn học: ('DSTT', 'ToanRR', 'LaptrinhCB', 'ToanCC')
#Danh sách điểm: (9, 8, 7, 10)

import itertools
tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
print("Kết quả tap_sinh:")
print(tap_sinh)
#[0, 1, 2, 3, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19]

kq = list(zip(range(4), range(7, 12), reversed(range(11))))
print("Kết quả zip ba tập:")
print(kq)
#range(4) → [0, 1, 2, 3]
#range(7, 12) → [7, 8, 9, 10, 11]
#reversed(range(11)) → [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

a = b = c = 0
mylist = []
execfile('d:/Lab1_PhamPhuVinh_2474802010441/thucthi1.py')
#Do lưu ổ D nên e mở đặt link ở ổ D
#100 200 300

from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f.simplify())  
# Kết quả sẽ là 3*x + 2

from sympy import Symbol
a = Symbol('Noi')
b = Symbol('Chim')
expr = 3*b + 7*a
print(expr)
# Kết quả là 3*Chim + 7*Noi

from sympy import Symbol
a = Symbol('Noi')
b = Symbol('Chim')
print(a.name)
print(b.name)
# Noi
# Chim

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
# Kết quả là 2*x*y

from sympy import Symbol
x = Symbol('x')
p = x * (x + 2 * x)
print(p)
#Kết quả là 3*x**2

from sympy import Symbol, simplify
x = Symbol('x')
y = Symbol('y')
p = (x + 2)*(y + 3) + (x + 2)*(x - 3)
p = simplify(p)
print("p =", p)
#Kết quả là p = (x + 2)*(x + y)

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)
# Kết quả là x2 - x*y + y2

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
giatri = bieuthuc.subs({x: 3, y: 2})
print(giatri)
# Kết quả là 7

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
giatri = bieuthuc.subs({x: 3, y: 2})
print(giatri)
print(x)
print(y)
#Kết quả là 7, x, y

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
giatri = bieuthuc.subs({x: 3, y: x})
print(giatri)
#Kết qả là x**2 - 3*x + 9

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
giatri = bieuthuc.subs({x: y, y: 3})
print(giatri)
#KẾT quả là 3

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
giatri = bieuthuc.subs({y: x}).subs({x: 3})
print(giatri)
#Kết quả là 9

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print(bieuthuc_moi)
#Kết quả là y**2 - y*(1 - y) + (1 - y)**2

from sympy import simplify
dongian = simplify(bieuthuc_moi)
print(dongian)
#Kết quả alf 3y**2 - 3y + 1

from sympy import Symbol, sin, cos, simplify
x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)
#Kết quả là sin(x + y)

import numpy as np
vec1 = np.array([1., 3., 5.])
vec1 * 2         
# [ 2.  6. 10.]
vec1 * vec1      
# [ 1.  9. 25.]
vec1 / 2         
# [0.5 1.5 2.5]
vec1 + vec1      
# [ 2.  6. 10.]

vec2 = np.array([2., 4.])
# vec1 + vec2    
#không thể cộng hai vector có độ dài khác nhau

vec3 = np.array([2., 4., 6.])
vec1 + vec3      
# [ 3.  7. 11.]
vec1 / vec3      
# [0.5        0.75       0.83333333]
vec1 * vec3      
# [ 2. 12. 30.]
2*vec1 + 5*vec3  
# [12. 26. 40.]

vec3[2]          
# 6.0

vec4 = np.linspace(0, 20, 5)
vec4             
# [ 0.  5. 10. 15. 20.]
vec5 = np.zeros(5)
vec5             
# [0. 0. 0. 0. 0.]
vec6 = np.ones(5)
vec6             
# [1. 1. 1. 1. 1.]
vec7 = np.empty(5)
vec7             
# [1. 1. 1. 1. 1.]  # Giá trị có thể khác nhau tùy hệ thống
vec8 = np.random.random(5)
vec8             
# [0.9889 0.5602 0.2719 0.6948 0.1608]  # Ngẫu nhiên

v = np.array([1., 3., 5.])
np.sum(v)        
# 9.0
v.shape          
# (3,)
v.transpose()    
# [1. 3. 5.]

v1 = v[:2]
v1               
# [1. 3.]
v[0] = 5
v                
# [5. 3. 5.]
v1               
# [5. 3.]

# v1[:2] = [1., 2., 3.]  # Lỗi - không thể gán 3 phần tử vào 2 vị trí
v1[:2] = [1., 2]
v                
# [1. 2. 5.]

v3 = 2 * v[:2] + v1 * 3
v3               
# [ 5. 10.]
v1 = [4, 6]
v3               
# [ 5. 10.]

v + 10.0         
# [11. 12. 15.]
np.sqrt(v)       
# [1.         1.41421356 2.23606798]
np.cos(v)        
# [ 0.54030231 -0.41614684  0.28366219]
np.sin(v)        
# [ 0.84147098  0.90929743 -0.95892427]

np.dot(v1, v3)   
# 80.0
# v1.dot(v3)     
# # Lỗi - v1 là list, không có phương thức dot
v3.dot(v1)       
# 80.0

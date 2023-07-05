import numpy as np
import sympy as sp


a = 0.5
b = 1.0
h = (b-a)/10
arr_x = [round(a + i*h, 2) for i in range(11)]
n = 4
k = 1
m = 3
x = sp.Symbol('x')

# function
fun_x = lambda x: x**2 - np.sin(x)


def create_table(fun, arr_x):
    arr_y = [fun(arr_x[i]) for i in range(len(arr_x))]
    return arr_y

arr_y = create_table(fun_x, arr_x)

def la_poly(arr_x, arr_y, n):
    L = 0
    for k in range(n):
        part = arr_y[k]
        num = 1.0
        den = 1.0
        for j in range(n):
            if (j != k):
                num *= (x - arr_x[j])
                den *= (arr_x[k] - arr_x[j])
        a = num / den
        part *= a
        L += part 
    return L
 

L4 = la_poly(arr_x, arr_y, n + 1)
dfdx = sp.diff(L4, x, k)
print(f"L'4 = {dfdx}")
Lxm = dfdx.subs(x, arr_x[m])
print(f"L4'({arr_x[m]}) = {Lxm}")
 
y = x**2 - sp.sin(x)
dydx = sp.diff(y, x, k)
yxm = dydx.subs(x, arr_x[m])
print(f"y'({arr_x[m]}) = {yxm}")
 
w5 = 1.0
for i in range(n+1):
    w5 *= (x - arr_x[i])
minf = sp.diff(y, x, n + 1).subs(x, arr_x[n]) 
maxf = sp.diff(y, x, n + 1).subs(x, arr_x[0]) 
minR4 = minf * sp.diff(w5, x, k).subs(x, arr_x[m]) / np.math.factorial(n + 1)
maxR4 = maxf * sp.diff(w5, x, k).subs(x, arr_x[m]) / np.math.factorial(n + 1)
R = Lxm - yxm
print(f'minR4 = {minR4}', f'maxR4 = {maxR4}', f'R = Lxm - yxm = {R}', sep='\n')
print(f'minR4 < R4 < maxR4 - {abs(minR4) < abs(R) < abs(maxR4)}')
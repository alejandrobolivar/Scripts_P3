import sympy as sp
x = sp.Symbol('x')
int1 = sp.Integral( sp.sin(x)**3 /(2*x), x)
print(sp.latex(int1))
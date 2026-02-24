import numpy as np

# 1) Criar dois arrays, somar, subtrair e multiplicar cada elemento

a = np.array([2, 5, 7])
b = np.array([1, 0, 3])
soma = a+b
sub = a-b
mlt = a*b

print("Resultados questão 1:")
print(soma)
print(sub)
print(mlt)

# 2) Para um array de exemplo, achar o número de dimensões, formato e elementos no total

m = np.array([[1, 2, 3], [4, 5, 6]])
print("Resultados questão 2:")
print(m.ndim)
print(m.shape)
print(m.shape[0] * m.shape[1])

# 3) Dado um array de exemplo, use reshape para transformar em 4x2, 2x4 e 3x3
x = np.array([1,2,3,4,5,6,7,8])

x1 = x.reshape((4,2))
x2 = x.reshape((2,4))
print("Resultados questão 3:")
print(x1)
print(x2)
print("Para reshape(3,3), seriam necessários 9 elementos, só temos 8")

# Potencia e raiz quadrada
print("Funções >>>")

def potencia(x,n):
    ctt = x
    for i in range (1, n):
        ctt = ctt*x
    return ctt

def raiz(x,n):
    root = 1/n
    
    result = x**root
    return result

print("Potencia de x elevado a n: ", potencia(4, 4))

print("Raiz n de x:", raiz(27, 3))





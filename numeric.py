import numpy as np

# apenas anotacoes da seção python numérico isl

# arrays

print("Arrays")
x = np.array([3, 4, 5])
y = np.array([4, 9, 7])

print(x+y)

# array de duas dimensões

print("Arrays de duas dimensões")
z = np.array([[1,2], [3, 4]])

print("valores: ", z)
print("Dimensões: ", z.ndim)
print("Linhas e colunas: ", z.shape)

# Métodos
print("Métodos usados em objetos")
x = np.array([1, 2, 3, 4])
a = x.sum()
print(x)
print("Método sum() soma tudo de x:", a)

# método reshape
print("Método reshape() retorna um novo array com os mesmos elementos de x em um formato diferente")

x = np.array([1,2,3,4,5,6])
print("Começou x:\n", x)
# Colocar pra duas dimensões de 2 linhas e 3 colunas
x_reshaped = x.reshape((2,3))
print("Novo formato de X:\n", x_reshaped)

# Gerar dados aleatórios
print("Gerar dados aleatórios")
print("1) Função np.random.normal(loc, scale, size)\nServe para gerar size valores com media = loc e desvio padrão scale. Por padrão, definimos apenas size e os valores são N(0,1)")

x = np.random.normal(size=10)
print(x)

print("Com x, podemos criar outro array y somando x + valores aleatórios")
y = x + np.random.normal(loc=50, scale=2, size=10)
print(y)
print("Printar a correlação entre x e y: np.corrcoef(x,y))")

print("Correlação:", np.corrcoef(x,y))

# Dados aleatórios com seed
print("Temos utilizado o np.random.normal(), mas se quisermos usar um valor arbitrário como seed para gerar valores, temos a função default_rng()")

rng = np.random.default_rng(3)
print(rng.normal(scale=1, size=2))

# Média, desvio padrão e variancia
print("Para média, desvio padrão e variancia, temos mean(), var(), std()")

rng=np.random.default_rng(3)
y = rng.standard_normal(10)
print(np.mean(y), y.mean())

X = rng.standard_normal((4,3))
print(X)

# Axis
# Para matrizes, as funções se referem à dimensões como axis. axis=0 são as linhas, enquanto axis=1 são as colunas



from random import randint

###
# Tentativa de fazer a fórmula da taxa de erros, que mede a qualidade do treinamento para dados qualitativos
# Taxa de Erros = 1/n * somatorio de I(yi != yli), em que I() é uma função que retorna 1 caso yi seja diferente de yli
#

def indicator(yi, yli):
    if yi != yli:
        return 1
    return 0

N = 100

y = [randint(1,10) for _ in range(N)]
yl = [randint(1,10) for _ in range(N)]

ctt = 0
for i in range(N):
    if indicator(y[i], yl[i]) == 1:
        ctt += 1

te = ctt/N

print(te)




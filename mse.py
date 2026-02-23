## Tentativa de gerar o Erro Quadrático Médio (MSE)
#
# Fórmula (acho) é MSE = 1/n * somatório de: (yi - yli)^2
from random import randint
import matplotlib.pyplot as plt


def mse(n):
    y = []
    yl = []
    
    for i in range(n):
        y.append(randint(1,100))
        yl.append(randint(1, 100))

    ctt=0
    for i in range(n):
#        print((y[i] - yl[i]) ** 2)
        ctt += (y[i] - yl[i])**2
    mse_value = ctt / n

    plt.plot(y[:10])
    plt.plot(yl[:10])
    plt.show()
#   return mse_value

#print(mse(100))
mse(100)



import random

# tentativa de fazer o knn
# apenas trazendo a ideia de forma rasa
# Tendo um valor K, e a amostra Xo (amostra de teste),
# o KNN cria uma lista com as K amostras de treinamento Xi mais próximas de
# Xo e usa uma função indicadora se essa amostra Xi = j.
# Então é feito um somatório de Xi=j com K, sendo a Pr de Xo.

# O primeiro passo é achar os K valores de treinamento xi 
# mais próximos de xo e identificar suas classes.

def achar_mais_proximos(k, xi, yi, xo):
    proximos = []
    for i in range(len(xi)):
        dist = abs(xo - xi[i])
        proximos.append((dist, i, yi[i]))
    proximos.sort()
    return proximos[:k]

K = 5

xi=[random.uniform(1.0, 10.0) for _ in range(100)]
yi=[random.choice(['A','B']) for _ in range(100)]

xo=4.3
j = 'A'

k_proximos = achar_mais_proximos(K, xi, yi, xo)


# Com essas definições, criamos a função indicadora
# ela é I(yi=j), que retorna 1 se yi=j e 0 caso contrario.

def indicadora(k_proximos, j):
    ctt=0
    for i in k_proximos:
        if i[2]==j:
            ctt+=1
    return ctt

# Para implementar a probabilidade de Bayes, fazemos a fórmula:
# Pr(Y=j|X=xo) = 1/K * somatorio de I(yi=j)

ctt = indicadora(k_proximos, j)
prob = ctt/K

print(prob)

# Modificação para calcular todas as classes possíveis
# e não apenas a de j='A'

classes = set(yi)
def prob_classes(classes):
    probabilidades = {}
    
    for classe in classes:
        p = indicadora(k_proximos, classe)
        probabilidades[classe] = p/K
        
    return probabilidades

print(prob_classes(classes))










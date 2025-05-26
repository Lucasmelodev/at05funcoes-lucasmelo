# 1) Função para calcular o IMC
def calcula_imc(peso=70, altura=1.75):
    return peso / (altura ** 2)

imc = calcula_imc()
print("IMC:", imc)

# 2) Trabalhando com a lista de alturas
alturas = [45, 23, 67, 12, 11, 89, 23, 41, 50, 62, 78, 34, 56, 19, 72, 88, 11, 90, 39, 65,
           76, 27, 48, 59, 81, 14, 11, 93, 3, 68, 29, 52, 74, 16, 85, 20, 55, 38, 69, 11,
           83, 7, 44, 61, 18, 96, 22, 58, 31, 71, 40, 53, 87, 31]

print("Maior valor:", max(alturas))
print("Menor valor:", min(alturas))
print("Soma de todos os valores:", sum(alturas))
print("Valor absoluto de -25:", abs(-25))
print("Número 3.14159 arredondado para 2 casas decimais:", round(3.14159, 2))

import statistics

print("Média:", statistics.mean(alturas))
print("Mediana:", statistics.median(alturas))
print("Moda:", statistics.mode(alturas))
print("Variância:", statistics.variance(alturas))
print("Desvio padrão:", statistics.stdev(alturas))

# 3) Criando matrizes aleatórias
import random

matriz1 = []
for i in range(5):
    linha = []
    for j in range(10):
        linha.append(random.random())
    matriz1.append(linha)

print("\nMatriz 5x10 de float aleatórios:")
for linha in matriz1:
    print(linha)

matriz2 = []
for i in range(8):
    linha = []
    for j in range(4):
        linha.append(random.randint(0, 9))
    matriz2.append(linha)

print("\nMatriz 8x4 de inteiros aleatórios:")
for linha in matriz2:
    print(linha)

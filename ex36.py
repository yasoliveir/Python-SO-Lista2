#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

n = int(input('Número: '))
soma = 1
fatorial = 1 #variavel acumuladora para a multiplicação
for i in range (1, n+1):
    fatorial = fatorial * i #a cada passagem do for ele ganha o novo valor acumulado
    soma += 1 / fatorial #adiciona 1 / i! na soma

print(f"O resultado da série para N = {n} é {soma:.2f}")

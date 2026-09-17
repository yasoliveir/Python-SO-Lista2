#Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
soma = 0

for i in range (maior, menor-1, -1):
    if (i % 2 != 0):
        impar = i
        soma += i
        print(impar)
print(f'A soma entre os números ímpares de {maior} para {menor} é: {soma}')

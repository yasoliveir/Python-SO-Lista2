#Receba um número inteiro. Calcule e mostre o seu fatorial.

n = int(input('Numero: '))
aux = n
cont = n
for i in range(n-1, 0, -1):
    aux = i * aux
    print(f'O resultado de {cont}! é: {n}x{i} = {aux}')
    n = aux
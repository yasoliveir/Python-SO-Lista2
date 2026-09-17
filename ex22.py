#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

x1 = int(input('Primeiro Número Inteiro: '))
x2 = int(input('Segundo Número Inteiro: '))

if x1 > x2:
    print(f'Ordem crescente dos números: {x1} | {x2}')
elif x1 < x2:
    print(f'Ordem crescente dos números: {x2} | {x1}')
else:
    print('Os números são iguais')
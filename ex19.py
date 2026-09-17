#Receba 2 valores reais. Calcule e mostre o maior deles.

x1 = float(input('Informe o primeiro número: '))
x2 = float(input('Informe o segundo número: '))

if x1 == x2:
    print('Os dois valores são iguais.')
elif x1 > x2:
    print(f'O maior número é {x1}')
else:
    print(f'O maior número é {x2}')

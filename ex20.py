#Receba 3 coeficientes A, B e C de uma equação do 2o grau da fórmula AX2+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

a = int(input('Coeficiente A: '))
b = int(input('Coeficiente B: '))
c = int(input('Coeficiente C: '))

delta = (b**2) - 4 * a * c
print()
if delta == 0:
    x1 = (-b + (delta**0.5)) / (2 * a)
    print(f'Valor de delta: {delta}. Há apenas uma raiz real, sendo ela {x1}')
elif delta > 0:
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)
    print(f'Valor de delta: {delta}. Há duas raizes reais, sendo X1: {x1} | X2: {x2}')
else: 
    print(f'Valor de delta negativo ({delta}), não há raizes reais')

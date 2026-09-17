 #Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

x1 = int(input('Informe o primeiro número: '))
x2 = int(input('Informe o segundo número: '))

if x1 == x2:
    print('Os dois valores são iguais.')
elif x1 > x2:
    dif = x1 - x2
    print(f'O número maior é {x1} e a diferença entre {x1} e {x2} é {dif}')
else:
    dif = x2 - x1
    print(f'O número maior é {x2} e a diferença entre {x2} e {x1} é {dif}')
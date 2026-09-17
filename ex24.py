#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
x = int(input('Valor inteiro: '))

if (x % 2 == 0) and (x % 3 == 0):
    print(f'O número {x} é divisível por 2 e 3')
elif (x % 2 == 0) and (x % 3 != 0):
    print(f'O número {x} é divisível apenas por 2')
elif (x % 2 != 0) and (x % 3 == 0):
    print(f'O número {x} é divisível apenas por 3')
else:
    print('O número nao é divisível por 2 nem por 3')
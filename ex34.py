#Receba um número. Calcule e mostre os resultados da tabuada desse número.
n = int(input('Numero: '))
cont = 1
for c in range (1, 11):
    
    result = cont * n
    print(f'{n} x {cont} = {result}')
    cont += 1
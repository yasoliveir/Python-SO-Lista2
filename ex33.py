 #Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.   

n = int(input('Numero: '))
serie = 0
cont = 1
for i in range (1, n+1):
    serie += (1/i)
    print(f'1 + 1/{cont} = {serie:.2f}')
    cont += 1
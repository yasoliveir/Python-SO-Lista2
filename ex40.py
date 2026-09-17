#Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

inicio = min(n1, n2)
fim = max(n1, n2)

print(f"\nNúmeros primos entre {inicio} e {fim}:")

for num in range(inicio, fim + 1):
    if num < 2:
        continue  # Números menores que 2 não são primos
    primo = True
    #Testando se o 'num' tem algum divisor além de 1 e dele mesmo
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break  # Se tiver um divisor, não é primo
            
    #Se nao tiver, é primo, exibe na tela
    if primo:
        print(num, end=" ")
print()  
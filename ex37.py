#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
n = int(input('Número de termos: '))
a = 0 #numero atual
b = 1 #prox numero

if n <= 0:
    print('O número de termos deve ser maior que 0')
elif n == 1:
    print('Série de Fibonacci = 0')
else:
    print('Série de Fibonacci:', end=' ')
    for i in range (n):
        print(a, end=' ')
        prox = a + b #guarda a soma dos dois, numero atual + prox
        a = b #atualiza o valor atual com o prox valor
        b = prox #atualiza o valor do prox numero com a soma guardada
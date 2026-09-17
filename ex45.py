#Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 - ... + 15/225

soma = 0.0

for n in range(1, 16):
    numerador = n
    denominador = n ** 2
    termo = numerador / denominador
    
    # Se 'n' for ímpar, soma (+); se for par, subtrai (-)
    if n % 2 != 0:
        soma += termo
    else:
        soma -= termo

print(f"Resultado da série: {soma:.4f}")
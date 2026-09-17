#Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

soma = 0.0

for n in range(1, 51):
    numerador = n
    denominador = 2 * n + 1
    soma += numerador / denominador

print(f"Resultado da série: {soma:.4f}")
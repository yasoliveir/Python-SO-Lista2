#Receba o número da base e do expoente. Calcule e mostre o valor da potência.

base = float(input("Digite o número da base: "))
expoente = int(input("Digite o expoente (inteiro): "))

potencia = base ** expoente

print(f"O resultado de {base} elevado a {expoente} é: {potencia}")
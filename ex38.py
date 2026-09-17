#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

maior = None
menor = None
contador = 0

print("Digite 100 números reais e positivos: ")

while contador < 100:
    num = float(input(f"Digite o {contador + 1}º número: ")) 
    if num <= 0:
        print("Digite apenas números reais positivos.")
        continue #retorna para o input
    
    if maior is None and menor is None:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    contador += 1

print("\n--- Resultado ---")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
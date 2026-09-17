#Calcule a quantidade de grãos contidos em um tabuleiro de xadrez

total = 0
graos_na_casa = 1

for casa in range(1, 65):
    total += graos_na_casa
    graos_na_casa *= 2  # Dobra para a próxima casa

print(f"Total de grãos acumulados: {total}")
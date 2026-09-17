#Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.

soma = 7
print(f"Combinações que somam {soma}:")

for dado1 in range(1, 7):
    for dado2 in range(1, 7):
        if dado1 + dado2 == soma:
            print(f"Dado 1: {dado1} | Dado 2: {dado2}")
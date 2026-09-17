#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

voltas = int(input('Número de voltas: '))
extensao = float(input('Extensão do circuito (em metros): '))
tempo = int(input('Duração (em minutos): '))

km = (extensao / 1000) * voltas
t = tempo / 60

vm = km / t
print()
print(f'Distância total: {km:.0f} km ')
print(f'Tempo total: {t:.1f} h ')
print(f'A velocidade média é de {vm:.2f} km/h')
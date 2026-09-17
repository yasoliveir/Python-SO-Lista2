#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
from datetime import datetime

h1 = input('Hora de início (HH:MM): ')
dt = datetime.datetime.strptime(h1, "%H:%M")


h2 = input('Hora de Término (HH:MM): ')
dt2 = datetime.datetime.strptime(h2, "%H:%M")

print(dt2)


# teste = dt2 - dt
# print(type(teste))

# if teste.seconds >= 86400:
#     print("passou de um dia")
# else:
#     print(f"Resultado: {teste}")


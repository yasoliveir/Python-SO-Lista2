#Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

altura_ana = 110
altura_maria = 150

taxa_ana = 3
taxa_maria = 2

anos = 0

# O laço continua enquanto Ana for menor ou igual a Maria
while altura_ana <= altura_maria:
    altura_ana += taxa_ana
    altura_maria += taxa_maria
    anos += 1

print(f"Serão necessários {anos} anos para Ana ser maior que Maria.")
print(f"Altura final de Ana: {altura_ana / 100:.2f} m")
print(f"Altura final de Maria: {altura_maria / 100:.2f} m")
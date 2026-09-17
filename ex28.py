#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço

preco_atual = float(input('Preço atual: '))
media_mensal = float(input('Média mensal: '))

if (preco_atual < 30.00) and (media_mensal < 500):
    preco_novo = preco_atual + (0.1 * preco_atual)
elif (preco_atual >= 30.00 and preco_atual  < 80.00) and (media_mensal >= 500 and media_mensal < 1000):
    preco_novo = preco_atual + (0.15 * preco_atual)
elif (preco_atual >= 80.00) and (media_mensal >= 1000):
    preco_novo = preco_atual - (0.05 * preco_atual)
else: 
    preco_novo = preco_atual
print(f'O valor do produto atualizado é de R${preco_novo}')
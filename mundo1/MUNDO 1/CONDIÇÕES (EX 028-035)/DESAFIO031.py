viagem = float(input('Digite a distância da viagem: '))
print(f'Você está prestes a começar uma viagem de {viagem} km.')
if viagem <= 200:
   preco = viagem * 0.50
else:
    preco = viagem * 0.45
print(f'O preço da sua passagem será de R$ {preco:.2f}')

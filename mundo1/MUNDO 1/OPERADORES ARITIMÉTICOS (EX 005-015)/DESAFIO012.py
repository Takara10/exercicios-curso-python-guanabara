valorori = float(input('Qual é o preço do produto? '))
valordesc = valorori * 0.05
valorfinal = valorori - valordesc
print(f'O produto que custava R${valorori:.2f}, na promoção com desconto de 5% vai custar R${valorfinal:.2f}')

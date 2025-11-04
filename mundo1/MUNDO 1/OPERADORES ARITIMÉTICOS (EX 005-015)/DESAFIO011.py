alt = float(input('Altura: '))
larg = float(input('Largura: '))
area = alt * larg
pintura = area / 2
print(f'Sua parede tem a dimensão de {alt} x {larg} e sua área é de {area}')
print(f'Para pintar essa parede, você precisara de {pintura:.2f}')

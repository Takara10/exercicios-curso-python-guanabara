medida = float(input('Digite a medida em metros: '))
cent = medida * 100
mil = medida * 1000
deci = medida * 10
hec = medida / 100
deca = medida / 10
kilo = medida / 1000
print(f' Na medida de {medida}m corresponde a:')
print(f'{cent:.0f}cm')
print(f'{mil:.0f}mm')
print(f'{deci:.0f}dm')
print(f'{hec:.0f}hm')
print(f'{deca:.0f}dam')
print(f'{kilo:.0f}km')

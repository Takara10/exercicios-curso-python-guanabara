cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.upper()
resultado = (cidade[:5]=='SANTO')
print(f'A cidade começa com "SANTO" ? {resultado}')

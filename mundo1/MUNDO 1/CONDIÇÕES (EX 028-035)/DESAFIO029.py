vermelho = '\033[31m'
verde = '\033[32m'
limpa = '\033[0m'
velocidade = float(input('Digite a velocidade que o carro atingiu: '))
if velocidade > 80:
    print(f'Você foi multado em {vermelho}R$ {(velocidade - 80) * 7 :.2f} {limpa} por ultrapassar a velocidade de 80 km/h!')
else:
    print(f'Tenha um bom dia! {verde}Dirija com segurança!{limpa}')


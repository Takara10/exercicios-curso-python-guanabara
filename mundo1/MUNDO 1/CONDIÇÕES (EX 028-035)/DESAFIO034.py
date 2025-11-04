sal = float(input('Digite o seu sálario R$: '))
if sal > 1250:
    novosalario = sal * 1.10
else:
    novosalario = sal * 1.15
print(f'Quem ganhava R$ {sal:.2f} passa a ganhar R$ {novosalario:.2f} agora.')
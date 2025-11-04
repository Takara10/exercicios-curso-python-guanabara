din = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = din/5.15
eur = din/6.36
iene = din/0.037
print(f'Com R${din:.2f} você pode comprar US$ {dol:.2f} ')
print(f'Com R${din:.2f} você pode comprar EUR$ {eur:.2f} ')
print(f'COm R${din:.2f} vcoê pode comprar IENE$ {iene:.2f} ')
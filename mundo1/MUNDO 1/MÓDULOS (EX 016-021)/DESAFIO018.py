import math

angulograus = float(input('Digite o ângulo em graus: '))

angulorad = math.radians(angulograus)
seno = math.sin(angulograus)
cosseno = math.cos(angulograus)
tangente = math.tan(angulograus)

print(f'Com o ângulo de {angulograus:.2f}')
print(f'O seno de {seno:.2f}')
print(f'O coseno de {cosseno:.2f}')
print(f'O tangente de {tangente:.2f}')

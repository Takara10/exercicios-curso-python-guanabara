num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
num3 = int(input('Digite o 3° valor: '))
menor = num1
maior = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')




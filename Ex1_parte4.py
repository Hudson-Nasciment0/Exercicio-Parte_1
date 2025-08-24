# Desenvolva um programa que leia uma lista de números e mostre a média deles 

numero = [10, 20, 30]

soma = 0

for i in numero:
    print(f'{i}')
    soma += i
    
media = soma / len(numero)
print(f'A média é de {media}')
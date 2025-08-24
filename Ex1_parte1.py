# Faça um programa que leia dois números e mostre qual é o maior

a = float(input('Digite um numero:'))
b = float(input('Digite outro numero:'))

def descobreMaiorNumero(a, b):
    if a > b:
        return a

    elif a == b:
        return None

    else:
        return b

if a > b:
    print(f'{a} é maior que {b}')

elif a == b:
    print(f'{a} e {b} são iguais!')

else:
    print(f'{b} é maior que {a}')

descobreMaiorNumero(a,b)


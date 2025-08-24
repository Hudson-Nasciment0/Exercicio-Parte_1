# 2.Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário. 

numero = int(input('Qual o Número Desejado?'))



for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
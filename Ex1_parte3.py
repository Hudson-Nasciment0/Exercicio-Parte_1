# 3.Crie uma função que verifique se um número é primo. 

def numero_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

verificar = int(input("Digite um numero para Verificar se é Primo:"))

if numero_primo(verificar):
    print(f'O numero {verificar} é Primo!')

else:
    print(f'O número {verificar} não é Primo')

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



















# def eh_primo(n):
#     if n < 2:
#         return False  # Números menores que 2 não são primos
#     # Testa todos os números de 2 até a raiz quadrada de n
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:  # Se n for divisível por i, não é primo
#             return False
#     return True  # Se não encontrou nenhum divisor, é primo

# numero = int(input("Digite um número para verificar se é primo: "))

# if eh_primo(numero):
#     print(f"{numero} é primo.")
# else:
#     print(f"{numero} não é primo.")
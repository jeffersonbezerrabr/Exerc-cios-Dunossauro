# Encontrar números primos é uma tarefa difícil. 
# Faça um programa que gera uma lista dos números primos existentes 
# entre 1 e um número inteiro informado pelo usuário.

primos = []

try:
    n = int(input("Digite um número para verificar todos os primos até o número informado: "))
    if n < 2:
        print("Não é primo")
    else:
        for c in range(2, n+1):
            eh_primo = True
            for t in range(2, c):
                if c % t == 0:
                    eh_primo = False
                    break
            if eh_primo:
                primos.append(c)
    print(primos)

except ValueError:
    print("Precisa digitar um número inteiro")
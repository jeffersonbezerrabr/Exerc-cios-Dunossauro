# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

primos = []
divisoes = 0
try:
    n = int(input("Digite um número: ")) 
    if n < 2:
        print("Não existem números primos nesse intervalo.")
    
    else:
        for num in range(2, n + 1):
            primo = True
            for div in range(2, num):
                divisoes += 1
                if num % div == 0:
                    primo = False
                    break
            if primo:
                primos.append(num)
    
except ValueError:
    print("Precisa digitar um número")

if primos: 
    print(f"Segue os números primos entre 1 e {n}: {primos}")
    print(f"Quantas divisões foram feitas: {divisoes}")
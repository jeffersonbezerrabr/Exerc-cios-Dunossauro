# Exercício 09

# Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

lista = []

while len(lista) < 10:
    try:
        n = int(input(f"Informe o {len(lista)+ 1}º número: "))
        lista.append(n)
    
    except ValueError:
        print("Precisa digitar um número inteiro!")
        continue
    
soma = [x ** 2 for x in lista]

print(f"A soma dos quadrados dos elementos:\n{soma}")
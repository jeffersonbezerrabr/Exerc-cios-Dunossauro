# Exercício 07

# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
mult = 1
while len(lista) < 5:
    try:
        n = int(input(f"Digite o {len(lista)+1}º número: "))
        lista.append(n)
    
    except ValueError:
        print("Precisa digitar um valor inteiro")

soma = sum(lista)

for m in lista:
    mult *= m
    
print("\n--- RESULTADOS ---")
print(f"Números digitados: {lista}")
print(f"Soma dos valores: {soma}")
print(f"Multiplicação dos valores: {mult}")
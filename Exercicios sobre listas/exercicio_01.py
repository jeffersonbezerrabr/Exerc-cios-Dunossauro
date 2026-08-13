# Exercício 01

# Faça um programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

while len(lista) < 5:
    try:
        n = int(input(f"Informe o {len(lista) + 1}º Número: "))
        lista.append(n)
        
    except ValueError:
        print("Precisa informar um número inteiro.")
        continue
    
print(lista)
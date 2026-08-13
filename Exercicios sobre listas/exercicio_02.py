# Exercício 02

# Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

while len(lista) < 10:
    try:
        n = int(input(f"Informe o {len(lista) + 1}º Número: "))
        lista.append(n)
        
    except ValueError:
        print("Precisa informar um número inteiro.")
        continue
    
reverso = lista
reverso.reverse()
print(reverso)
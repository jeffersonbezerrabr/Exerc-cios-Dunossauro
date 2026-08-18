# Exercício 05

# Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


par = []
impar = []
numeros = []

while len(numeros) < 20:
    try:
        n = int(input(f"Informe o {len(numeros) + 1}º número: "))
        numeros.append(n)
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    except ValueError:
        print("Precisa digitar um valor inteiro!")
        
print(f"\nTodos os números digitados: {numeros}\n")
print(f"Números Pares: {par}\n")
print(f"Números Impares: {impar}")

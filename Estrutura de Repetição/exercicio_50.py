"""
Exercício 50

Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
Faça um programa que calcule o valor de H com N termos.
"""

total = 0

while True:
    try:
        n = int(input("Deseja verificar quantos n termos: "))
        if n <= 0:
            print("Precisa informar um valor positivo!")
            continue
        else:
            for c in range(1, n + 1):
                total += 1 / c
            break
    except ValueError:
        print("Precisa digitar um valor inteiro!")

print(f"Soma da série: {total:.2f}")

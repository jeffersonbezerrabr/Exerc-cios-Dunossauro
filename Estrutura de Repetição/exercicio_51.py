"""
Exercício 51

Faça um programa que mostre os n termos da Série a seguir:

S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

Imprima no final a soma da série.
"""

x = 1
total = 0
while True:
    try:
        n = int(input("Informe quantos n termos deseja: "))
        if n <= 0:
            print("Valor precisa ser positivo!")
            continue
        else:
            for c in range(1, n + 1):
                calc = c/x
                total += calc
                x += 2
            break
    
    except ValueError:
        print("Precisa digitar um valor inteiro!")
        
print(f"A soma da série é: {total:.2f}")

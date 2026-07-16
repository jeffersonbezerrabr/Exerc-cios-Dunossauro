"""
Exercício 49

Faça um programa que mostre os n termos da Série a seguir:

S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

Imprima no final a soma da série.
"""
x = 1
y = 1
total = 0
termos = []

while True:
    try:
        n = int(input("Deseja verificar quantos n termos: "))
        if n <= 0:
            print("Precisa informar um valor positivo!")
            continue
        else:
            # range(1, n + 1) garante que o loop rode exatamente 'n' vezes
            for c in range(1, n + 1):
                calc = x / y
                total += calc
                
                termos.append(f"{x}/{y}")
                
                x += 1
                y += 2
            break
    except ValueError:
        print("Precisa digitar um valor inteiro!")


print(f"\nSérie: {' + '.join(termos)}")
print(f"Soma da série: {total:.2f}")

# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = []
impares = []

x = 1

while x <= 10:
    n = input(f"Digite o {x}º número: ")
    try:
        int_n = int(n)
        if int_n % 2 == 0:
            pares.append(int_n)
            x += 1
        else:
            impares.append(int_n)
            x += 1
    except ValueError:
        print("Precisa digitar um número")
        continue
    
soma = (sum(pares) + sum(impares))

print(f"Lista dos números pares: {pares}\n")
print(f"Lista dos números impares: {impares}\n")
print(f"Soma dos números pares: {sum(pares)}\n")
print(f"Soma dos números impares: {sum(impares)}\n")
print(f"Soma de todos os números: {soma}")




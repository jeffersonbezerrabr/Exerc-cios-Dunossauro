# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro inteiro: "))
real = float(input("Digite um número real: "))

r1 = (n1 * 2) * (n2 / n2)
r2 = (n1 * 3) + real
r3 = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {r1}")
print(f"A soma do triplo do primeiro com o terceiro: {r2}")
print(f"O terceiro elevado ao cubo: {r3}")


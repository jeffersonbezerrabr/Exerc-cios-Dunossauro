# Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
x = 1

while x <= 5:
    n = input(f"Digite o {x}º Número: ")
    try:
        validar_n = float(n)
        lista.append(validar_n)
        x += 1
    except ValueError:
        print("Precisa digitar um número")
        continue
    
total = sum(lista)
media = total / len(lista)

print(f"A soma dos números informados é: {total}\n")
print(f"A média dos números informados é: {media}")

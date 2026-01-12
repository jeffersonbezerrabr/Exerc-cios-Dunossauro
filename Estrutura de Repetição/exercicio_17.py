# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120

while True:
    n = input("Informe um número inteiro para ver seu fatorial: ")
    try:
        int_n = int(n)
        if int_n > 0:
            break
        else:
            print("Precisa ser maior que 0")
            continue
    except ValueError:
        print("Precisa digitar um número inteiro")

soma = 1

for c in range(1, int_n + 1):
    soma *= c
print(soma)
        
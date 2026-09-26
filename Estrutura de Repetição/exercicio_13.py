# Faça um programa que peça dois números, base e expoente, 
# calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.


while True:
    n1 = input("Digite um número para base: ")
    try:
        f_n1 = int(n1)
    except ValueError:
        print("Precisa digitar um número.")
        continue
    n2 = input("Digite um número para o expoente: ")
    try:
        f_n2 = int(n2)
        break
    except ValueError:
        print("Precisa digitar um número.")
        continue
total = 1   
for c in range(int(n2)):
    total *= f_n1
print(total)

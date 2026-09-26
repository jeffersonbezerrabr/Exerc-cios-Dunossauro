# Faça um programa que leoa 5 números e informe o maior número.

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
    
print(f"O maior valor digitado foi {max(lista):.1f}")
    

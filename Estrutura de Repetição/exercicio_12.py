# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. 
# A saída deve ser conforme o exemplo abaixo:

"""
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

while True:
    n = input("Informe um número de 1 a 10 para ver sua tabuada: ")
    try:
        int_n = int(n)
        if int_n < 1 or int_n > 10:
            print("Precisa digitar um numero inteiro entre 1 e 10")
            continue
    except ValueError:
        print("Precisa digitar um número inteiro")
        continue
    break


print("Tabuada de adição:\n")
for s in range(1,11):
    print(f"{int_n} + {s} = {int_n + s}")
    
print(f"\nTabuada de subtração: \n")
for s in range(1,11):
    print(f"{int_n} - {s} = {int_n - s}")
    
print(f"\nTabuada de divisão: \n")
for s in range(1,11):
    print(f"{int_n} / {s} = {int_n / s}")

print(f"\nTabuada de multiplicação: \n")
for s in range(1,11):
    print(f"{int_n} * {s} = {int_n * s}")

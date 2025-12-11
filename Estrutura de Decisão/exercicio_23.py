# Faça um programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

# n = float(input("Digite um número: "))

# if n.is_integer():
#     print(f"{n} é um inteiro")
    
# else:
#     print(f"{n} é um float")

n = input("Digite um número: ")

try:
    numero = int(n)
    print("Número é inteiro")
 
except ValueError:
    try:
        numero = float(n)
        print("Numero float")
    except ValueError:
        print("Ops! Esse não é um número válido. Tente novamente...")

        


    

    

    
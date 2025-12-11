# Faça um programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias = {1:"Domingo",
        2:"Segunda",
        3:"Terça",
        4:"Quarta",
        5:"Quinta",
        6:"Sexta",
        7:"Sábado"}

while True:
    n = input("Digite um número de 1 a 7: ")
    try: 
        numero = int(n)
        if numero >= 1 and numero <=7:
            valor = dias[numero]
            print(valor)
            break
        else:
            print("Valor inválido")
        
    except ValueError:
        print("Digite um número válido")
        
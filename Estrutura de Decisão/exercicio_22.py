# Faça um programa que peça um número inteiro e determine 
# se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).


while True:
    n = input("Digite um número: ")
    try:
        int_n = int(n)
        if int_n <= 0:
            print("Precisa digitar um valor acima de 0")
            continue
        if int_n % 2 == 0:
            print(f"{int_n} é Par")
            break
        else:
            print(f"{int_n} é impar")
            break
    
    except ValueError:
        print("Digite um valor inteiro")
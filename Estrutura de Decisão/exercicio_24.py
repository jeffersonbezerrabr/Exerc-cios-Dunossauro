# Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    # par ou ímpar;
    # positivo ou negativo;
    # inteiro ou decimal.

operadores = ["+", "-", "*", "/"]
    
while True:
    n1 = input("Digite um número: ")
    try:
        numero1 = float(n1)
        break
    except ValueError:
        print("Precisa digitar um número!")
    
while True:
    n2 = input("Digite outro número: ")
    try:
        numero2 = float(n2)
        break
    except ValueError:
        print("Precisa digitar um número!")


while True:
    operacao = input("Qual operação deseja realizar? [+, -, *, /] ")

    if operacao not in operadores:
        print("Operação inválida!")
        continue
    
    if operacao == "/":
        if numero2 == 0:
            print("Erro: divisão por zero!")
            continue
    
    if operacao == "+":
        resultado = numero1 + numero2
        print(f"A soma de {numero1} + {numero2} é: ", end="")
        
    elif operacao == "-":
        resultado = numero1 - numero2
        print(f"A subtração de {numero1} - {numero2} é: ", end="")
        
    elif operacao == "*":
        resultado = numero1 * numero2
        print(f"A multiplicação de {numero1} * {numero2} é: ", end="")
    
    elif operacao == "/":
        resultado = numero1 / numero2
        print(f"A divisão de {numero1} / {numero2} é: ", end="")
        
    break

print(resultado)


# POSITIVO / NEGATIVO / ZERO
if resultado > 0:
    print(f"{resultado} é positivo")
elif resultado < 0:
    print(f"{resultado} é negativo")
else:
    print("É zero (nem positivo, nem negativo)")


# PAR / ÍMPAR
if resultado.is_integer():
    if resultado % 2 == 0:
        print(f"{resultado} é par")   
    else:
        print(f"{resultado} é impar")
else:
    print(f"{resultado} não é par nem ímpar por ser decimal")


# INTEIRO OU FLOAT
if resultado.is_integer():
    print(f"{resultado} é um número inteiro")   
else:
    print(f"{resultado} é um float")
    
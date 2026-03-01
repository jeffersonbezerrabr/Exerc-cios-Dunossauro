# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
# o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

"""
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
"""
operadores = ["+","-","*","/"]
while True:
    try:
        n = int(input("Montar a tabuada de: "))
        if n < 1:
            print("Valor precisa ser maior que 0")
            
        operacao = input("Qual operação deseja realizar [+, -, *, /]: ")
        if operacao not in operadores:
            print("Precisa digitar uma das 4 opções [+, -, *, /]")
            continue
        
        inicio = int(input("Deseja iniciar em que número: "))
        if inicio < 1:
            print("Valor precisa ser maior que 0")
            continue
        
        fim = int(input("Deseja terminar em que número: "))
        if fim < 1:
            print("Valor precisa ser maior que 0")
            continue
        elif fim < inicio:
            print("Valor final não pode ser menor que o inicial")
            continue
        
        for c in range(inicio, fim + 1):
            if operacao == "+":
                print(f"{n} + {c} = {n + c}")
            elif operacao == "-":
                print(f"{n} - {c} = {n - c}")
            elif operacao == "*":
                print(f"{n} * {c} = {n * c}")
            elif operacao == "/":
                print(f"{n} / {c} = {n / c:.2f}")
        break
    except ValueError:
        print("Precisa digitar um número inteiro")
    
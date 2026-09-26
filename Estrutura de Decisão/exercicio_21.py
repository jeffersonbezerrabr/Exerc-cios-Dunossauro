# Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do 
# saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis 
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece 
# duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece 
# três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1

maximo = 600
minimo = 10
nota100 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota1= 0

while True:
    valor = input("Quanto deseja sacar: ")
    try:
        f_valor = float(valor)
        if f_valor < minimo:
            print("Valor inferior ao valor minimo")
            print(f"Valor minimo: R$ {minimo:.2f}")
            
        elif f_valor > maximo:
            print("Valor superior ao valor maximo")
            print(f"Valor maximo: R$ {maximo:.2f}")
        
        else:
            break
    except ValueError:
        print("Precisa digitar um valor válido")

saldo = f_valor

while saldo >= 100:
    saldo -= 100
    nota100 += 1
    if saldo < 100:
        break
        
while saldo >= 50:
    saldo -= 50
    nota50 += 1
    if saldo < 50:
        break
        
while saldo >= 10:
    saldo -= 10
    nota10 += 1
    if saldo < 10:
        break
    
while saldo >= 5:
    saldo -= 5
    nota5 += 1
    if saldo < 5:
        break
    
while saldo >= 1:
    saldo -= 1
    nota1 += 1   
    if saldo == 0:
        break
 
if nota100 > 0:
    print(f"{nota100} Notas de 100")
if nota50 > 0:
    print(f"{nota50} Notas de 50")
if nota10 > 0:
    print(f"{nota10} Notas de 10")
if nota5 > 0:
    print(f"{nota5} Notas de 5")
if nota1 > 0:
    print(f"{nota1} Notas de 1")
    
        
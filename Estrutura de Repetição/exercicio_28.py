# Faça um programa que calcule o valor total investido por um colecionador 
# em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

while True:
    try:
        cds = int(input("Quantos Cds você tem na sua coleção: "))
        if cds < 1:
            print("Precisa informar um valor maior que 0")
        else:
            break
    except ValueError:
        print("Precisa digitar um valor númerico")
        
c = total_cds = 0

while c < cds:
    try:
        valor = float(input(f"Informe o valor do {c+1}º CD: "))
        if valor < 1:
            print("Valor do cd precisa ser positivo")
        else:
            total_cds += valor
            c += 1
    except ValueError:
        print("Precisa digitar um valor númerico!")
        
media = total_cds / cds
print(f"A Média por CD é R$ {media:.2f}")

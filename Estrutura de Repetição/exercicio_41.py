"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

while True:
    try:
        divida = float(input("Valor da dívida: "))
        if divida <= 0:
            print("Valor precisa ser maior que 0")
            continue
    except ValueError:
        print("Precisa informar um valor númerico")
        continue
    try:
        parcelas = int(input("Quantas parcelas: "))
        if parcelas <= 0:
            print("Parcelas precisa ser maior que 0")
            continue
    except ValueError:
        print("Precisa informar um valor númerico")
        continue
    break



print(f"{'Valor da Dívida':<20} {'Valor dos Juros':<20} {'Qntd Parcelas':<20} {'Valor Parcela':<20}")
print("-" * 80)
for c in range(1, parcelas + 1):
    juros_total = divida * 0.05 * (c - 1) 
    divida_juros = divida + juros_total
    valor_parcela = divida_juros / c
    print(f"{divida_juros:<20.2f} {juros_total:<20.2f} {c:<20} {valor_parcela:<20.2f}")

"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores: 
"""

"""
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
"""


contadores = [0 for _ in range(9)]

relacao = [
    "R$200 a R$299",
    "R$300 a R$399",
    "R$400 a R$499",
    "R$500 a R$599",
    "R$600 a R$699",
    "R$700 a R$799",
    "R$800 a R$899",
    "R$900 a R$999",
    "R$1000 em diante"
]

while True:
    try:
        vendas = float(input(
            "Digite as vendas brutas do vendedor (-1 para encerrar): "
        ))

        if vendas == -1:
            break

        if vendas < 0:
            print("Digite um valor positivo.")
            continue
        
        
        salario = 200 + (vendas * 0.09)
        

        if salario < 300:
            contadores[0] += 1
        elif salario < 400:
            contadores[1] += 1
        elif salario < 500:
            contadores[2] += 1
        elif salario < 600:
            contadores[3] += 1
        elif salario < 700:
            contadores[4] += 1
        elif salario < 800:
            contadores[5] += 1
        elif salario < 900:
            contadores[6] += 1
        elif salario < 1000:
            contadores[7] += 1
        else:
            contadores[8] += 1

    except ValueError:
        print("Digite um valor numérico válido.")

print("\nRelação dos vendedores:\n")

combinado = list(zip(relacao, contadores))

for faixa, quantidade in combinado:
    if quantidade == 1:
        print(f"Na faixa de {faixa}: {quantidade} vendedor")
    else:
        print(f"Na faixa de {faixa}: {quantidade} vendedores")

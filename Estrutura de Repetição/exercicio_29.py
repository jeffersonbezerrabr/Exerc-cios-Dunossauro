# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela 
# que contém o número de itens que o cliente comprou e ao lado o valor da conta. 
# Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente 
# está levando e olhar na tabela de preços. 
# Você foi contratado para desenvolver o programa que monta esta tabela de preços, 
# que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

"""
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
"""
valor_unidade = 1.99
total = 0
# while True:
#     try:
#         produtos = int(input("Quantos produtos vai comprar: "))
#         if produtos < 0:
#             print("Precisa informar ao menos 1 produto!")
#         elif produtos == 0:
#             print("Obrigado por nos visitar!")
#             exit()
#         else:
#             total = produtos * valor_unidade
#             break
#     except ValueError:
#         print("Precisa digitar um valor númerico!")       

# if total > 0:
#     print(f"Quantidade de produtos: {produtos}")
#     print(f"Valor a pagar: R$ {total:.2f}")
#     print("\n Obrigado pela preferência")

n = input("Aperte qualquer tecla para gerar a tabela de preço: \n")

print("Lojas Quase Dois - Tabela de preços\n")
for c in range(1,51):
    print(f"{c} produto(s) = R$ {c * valor_unidade:.2f}")
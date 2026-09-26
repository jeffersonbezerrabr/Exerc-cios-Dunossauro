# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: 

"""
                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
"""

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
# e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo = {1:"File duplo", 2:"Alcatra", 3:"Picanha"}


while True:
    tipo_carne = input("[1] - File Duplo\n"
                   "[2] - Alcatra\n"
                   "[3] - Picanha\n"
                   "Informe qual tipo de carne deseja: ")
    try:
        cod_carne = int(tipo_carne)
        if cod_carne in [1,2,3]:
            break
        else:
            print("Precisa digitar uma das opções: [1,2,3]")
    except ValueError:
        print("Precisa digitar um valor númerico")
        
while True:
    quantidade = input("Quantos Kg: ")
    try:
        num_quantidade = float(quantidade)
        if num_quantidade <= 0:
            print("Precisa digitar um valor acima de 0")
        else:
            break
    except ValueError:
        print("Precisa digitar um valor númerico:")

while True:
    cartao = input("A compra será no cartão tabajara?\n"
                   "[S]im ou [N]ão: ").upper()
    if cartao[0] not in "SN":
        print("Precisa digitar [S] para sim ou [N] para não")
    elif cartao[0] in "SN":
        desconto = 0.05
        break
    
if cod_carne == 1:
    if num_quantidade <= 5:
        preco_carne = 4.90
        valor = preco_carne * num_quantidade
    else:
        preco_carne = 5.80
        valor = preco_carne * num_quantidade


elif cod_carne == 2:
    if num_quantidade <= 5:
        preco_carne = 5.90
        valor = preco_carne * num_quantidade
    else:
        preco_carne = 6.80
        valor = preco_carne * num_quantidade

            
elif cod_carne == 3:
    if num_quantidade <= 5:
        preco_carne = 6.90
        valor = preco_carne * num_quantidade
    else:
        preco_carne = 7.80
        valor = preco_carne * num_quantidade

if cartao[0] == "S":
    valor_desconto = valor * desconto
    valor_com_desconto = valor - valor_desconto
            
    
print(f"""
Tipo escolhido: {tipo.get(cod_carne)}
Peso: {num_quantidade} Kg
Preço Total: R$ {valor:.2f}""",end="")
if cartao[0] == "S":
    print(f"""
Forma de pagamento: Cartão Tabajara
Valor do Desconto: R$ {valor_desconto:.2f}
Valor a Pagar: R$ {valor_com_desconto:.2f}
          """)
else:
    print(f"""
Forma de pagamento: Outros
Valor a pagar: R$ {valor:.2f}""")


# Exercício 43

# O cardápio de uma lanchonete é o seguinte: 

"""
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
"""

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

PRODUTOS = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00),
}

sub_total = 0
total_geral = 0
item = 1

pedidos = []

while True:
    try:
        pedido = int(input("Digite o código do pedido [0 para sair]: "))
        if pedido == 0:
            break
        
        elif pedido not in PRODUTOS:
            print("Precisa digitar um dos códigos disponíveis!")
            continue
        
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade precisa ser um valor positivo!")
            continue
        
        nome, preco = PRODUTOS[pedido]
        
        sub_total = preco * quantidade
        print(f"\nItem {item} - {nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor R$ {sub_total:5.2f}\n")
        item += 1
        total_geral += sub_total
        
        pedidos.append({
            "produto": nome,
            "quantidade": quantidade,
            "subtotal": sub_total
        })
        
        
    except ValueError:
        print("Precisa digitar um valor inteiro!")
        
print("\n=== CUPOM FISCAL ===")

for pedido in pedidos:
    print(
        f"{pedido["produto"]} "
        f"{pedido["quantidade"]} "
        f"R$ {pedido["subtotal"]:.2f}"
    )
        
print(f"\nTotal: R$ {total_geral:5.2f}")

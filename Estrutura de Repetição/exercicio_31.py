# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 
# e agora possui uma loja de conveniências. Faça um programa que implemente 
# uma caixa registradora rudimentar. 
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
# Um valor zero deve ser informado pelo operador para indicar o final da compra. 
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro 
# que o cliente forneceu, para então calcular e mostrar o valor do troco. 
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
# A saída deve ser conforme o exemplo abaixo:

"""
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
"""

print("Lojas Tabajara")
produtos = []
p = 1
while True:
    try:
        valor = float(input(f"Valor do Produto {p}: (0 para encerrar a compra!) R$ "))
        if valor < 0:
            print("Precisa digitar um valor positivo ou 0 para finalizar.")
        elif valor == 0:
            total = sum(produtos)
            for c,d in enumerate(produtos):
                print(f"Produto {c + 1}: R$ {d:.2f}")
            print(f"Total: R$ {total:.2f}")
            while True:
                try:
                    dinheiro = float(input("Informe o valor em dinheiro: R$ "))
                    print(f"Dinheiro: R$ {dinheiro:.2f}")
                    if dinheiro < total:
                        print(f"Está faltando R$ {total - dinheiro:.2f}")
                    elif dinheiro == total:
                        troco = 0
                        print(f"Troco: R$ {troco:.2f}")
                        p = 1
                        produtos.clear()
                        break
                    else:
                        troco = dinheiro - total
                        print(f"Troco: R$ {troco:.2f}")
                        p = 1
                        produtos.clear()
                        break
                except ValueError:
                    print("Precisa informar um valor númerico!")
        else:
            produtos.append(valor)
            p += 1
    except ValueError:
        print("Precisa digitar um número!")
    
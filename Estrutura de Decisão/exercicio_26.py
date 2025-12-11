# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    # Álcool:

        # até 20 litros: desconto de 3% por litro
        
        # acima de 20 litros: desconto de 5% por litro
    
    # Gasolina:
    
        # até 20 litros: desconto de 4% por litro
        
        # acima de 20 litros: desconto de 6% por litro
        
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

VALOR_ALCOOL = 1.90
VALOR_GASOLINA = 2.50

while True:
    tipo = input("Deseja abastecer com: "
             "[Á]lcool ou [G]asolina? ").lower()
    if tipo[0] not in "ag":
        print("Voce precisa digitar [A] para Álcool ou [G] para gasolina")
    else:
        break

while True:
    qntd = input("Quantos litros? ")
    try:
        n_qntd = float(qntd)
        break
    except ValueError:
        print("Precisa digitar um valor númerico")

total = 0

if tipo[0] == "a" and n_qntd <= 20:
    desconto = 0.03

    
elif tipo[0] == "a" and n_qntd > 20:
    desconto = 0.05

    
elif tipo[0] == "g" and n_qntd <= 20:
    desconto = 0.04

    
elif tipo[0] == "g" and n_qntd > 20:
    desconto = 0.06
    

print()   

if tipo[0] == "a":
    valor_sem_desconto = (VALOR_ALCOOL * n_qntd) 
    valor_desconto = valor_sem_desconto * desconto
    total = valor_sem_desconto - valor_desconto
    print(f"Tipo de combustível: Álcool")
    print(f"Quantidade em litros: {n_qntd}")
    print(f"Valor a pagar: R$ {total}")
    print(f"Você economizou: R$ {valor_desconto}")
    
else:
    valor_sem_desconto = (VALOR_GASOLINA * n_qntd) 
    valor_desconto = valor_sem_desconto * desconto
    total = valor_sem_desconto - valor_desconto
    print(f"Tipo de combustível: Gasolina")
    print(f"Quantidade em litros: {n_qntd}")
    print(f"Valor a pagar: R$ {total}")
    print(f"Você economizou: R$ {valor_desconto}")

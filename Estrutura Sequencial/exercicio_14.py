# João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca 
# do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos 
# além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

VALOR_MULTA = 4
PESO_MAX = 50

quilos = float(input("Quantos Kg Você pescou hoje? "))

if quilos > PESO_MAX:
    excedente = quilos - PESO_MAX
    multa = excedente * VALOR_MULTA
    if multa < 1:
        multa = 4
    print(f"Você excedeu {excedente}Kg do limite.")
    print(f"Segue valor da sua multa: R$ {multa}")
    
elif quilos == PESO_MAX:
    print("Tudo certo. Você pescou no limite.")
    print("Nenhuma multa a pagar.")

else:
    print("Tudo certo. Você pescou menos que o limite.")
    print("Nenhuma multa a pagar.")

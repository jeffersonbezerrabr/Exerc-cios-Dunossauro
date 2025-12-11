# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

"""
                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
"""

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a 
# quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


while True:
    quilos1 = input("Quantos Kg de morango deseja comprar? ")
    try:
        n_quilos1 = float(quilos1)
        break
        
    except ValueError:
        print("Precisa digitar um valor númerico")
        
while True:
    quilos2 = input("Quantos Kg de maça deseja comprar? ")
    try:
        n_quilos2 = float(quilos2)
        break
        
    except ValueError:
        print("Precisa digitar um valor númerico")
        
if n_quilos1 <= 5:
    morango = 2.50 
else: 
    morango = 2.20 
total1 = n_quilos1 * morango

if n_quilos2 <= 5:
    maca = 1.80
else:
    maca = 1.50
total2 = n_quilos2 * maca

total_total = total1 + total2
total_quilos = n_quilos1 + n_quilos2
    
if total_total >= 25 or total_quilos > 8:
    desconto = 0.10
    desconto_valor = total_total * desconto
    print(f"Você ganhou um desconto de 10%")
    print(f"Total a pagar: R$ {total_total - desconto_valor}")
    
else:
    print(f"Total a pagar: R$ {total_total}")


    

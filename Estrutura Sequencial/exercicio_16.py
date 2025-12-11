# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Informe o tamanho em metros quadrados: "))
litros_usados = area / 3
LITROS_LATA = 18
VALOR_LATA = 80
RENDIMENTO_LATA = 54

if area <= RENDIMENTO_LATA:
    print(f"Litros necessários: {litros_usados:.2f}")
    print(f"Necessário uma lata")
    print(f"Valor R$ {VALOR_LATA}")
    
else:
    print(f"Litros necessários: {litros_usados:.2f}")
    latas = int(litros_usados / LITROS_LATA)
    if latas != 0:
        latas += 1
    print(f"Quantidade de latas: {latas}")
    print(f"Valor R$ {VALOR_LATA * latas}")  
    

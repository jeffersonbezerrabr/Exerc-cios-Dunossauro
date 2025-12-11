# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # comprar apenas latas de 18 litros;
    # comprar apenas galões de 3,6 litros;
    # misturar latas e galões, de forma que o desperdício de tinta seja menor. 
    # Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
    
import math
    
area = float(input("Informe o tamanho em metros quadrados: "))
litros_usados = area / 6
litros_usados *= 1.1
LITROS_LATA = 18
VALOR_LATA = 80
LITROS_GALAO = 3.6
VALOR_GALAO = 25
lata = math.ceil(litros_usados / 18)
galao = math.ceil(litros_usados / 3.6)

latas_inteiras = int(litros_usados // 18)
resto = litros_usados - (latas_inteiras * LITROS_LATA)
litros_cobertos = latas_inteiras * 18
galoes_necessarios = math.ceil(resto / LITROS_GALAO)


valor_mistura = (latas_inteiras * VALOR_LATA) + (galoes_necessarios * VALOR_GALAO)

print(f"\n=== RESULTADOS ===")
print(f"Litros necessários (com folga): {litros_usados:.2f}L\n")

print(f"1) Apenas latas:")
print(f"   - Quantidade: {lata}")
print(f"   - Custo: R$ {VALOR_LATA * lata:.2f}\n")

print(f"2) Apenas galões:")
print(f"   - Quantidade: {galao}")
print(f"   - Custo: R$ {VALOR_GALAO * galao:.2f}\n")

print(f"3) Mistura:")
print(f"   - {latas_inteiras} latas e {galoes_necessarios} galões")
print(f"   - Custo total: R$ {valor_mistura:.2f}")

    
    
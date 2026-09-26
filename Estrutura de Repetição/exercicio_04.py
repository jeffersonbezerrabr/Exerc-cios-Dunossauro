# Supondo que a população de um país A seja da ordem de 80_000 habitantes 
# com uma taxa anual de crescimento de 3% e que a 
# população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários 
# para que a população do país A ultrapasse ou iguale a população do país B, 
# mantidas as taxas de crescimento.

populacao_pais_a = 80000
populacao_pais_b = 200000
anos = 0
TAXA_CRESCIMENTO_A = 0.03
TAXA_CRESCIMENTO_B = 0.015

while populacao_pais_a < populacao_pais_b:
    populacao_pais_a += (populacao_pais_a * TAXA_CRESCIMENTO_A)
    populacao_pais_b += (populacao_pais_b * TAXA_CRESCIMENTO_B)
    anos += 1
    
print(anos)
    
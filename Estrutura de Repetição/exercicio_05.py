# Altere o programa anterior permitindo ao usuário informar 
# as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

"""
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
"""
CONTINUE = True

while CONTINUE:
    anos = 0

    while True:
        populacao_pais_a = input("Informe a população do país A: ")
        try:
            valor_populacao_pais_a = float(populacao_pais_a)
            if valor_populacao_pais_a <= 0:
                print("Informe um valor positivo")
                continue
        except ValueError:
            print("O valor informado precisa ser númerico")
            continue
        break


    while True:
        taxa_crescimento_a = input("Informe a taxa a porcentagem da taxa de crescimento da população A: ")
        try:
            valor_taxa_crescimento_a = float(taxa_crescimento_a)
            if valor_taxa_crescimento_a <= 0:
                print("Informe um valor positivo")
                continue
        except ValueError:
            print("O valor informado precisa ser númerico")
            continue
        break  

    while True:
        populacao_pais_b = input("Informe a população do país B: ")
        try:
            valor_populacao_pais_b = float(populacao_pais_b)
            if valor_populacao_pais_b <= 0:
                print("Informe um valor positivo")
                continue
        except ValueError:
            print("O valor informado precisa ser númerico")
            continue
        break

    while True:
        taxa_crescimento_b = input("Informe a taxa a porcentagem da taxa de crescimento da população B: ")
        try:
            valor_taxa_crescimento_b = float(taxa_crescimento_b)
            if valor_taxa_crescimento_b <= 0:
                print("Informe um valor positivo")
                continue
        except ValueError:
            print("O valor informado precisa ser númerico")
            continue
        break 

    while valor_populacao_pais_a < valor_populacao_pais_b:
        valor_populacao_pais_a += (valor_populacao_pais_a * (valor_taxa_crescimento_a /100))
        valor_populacao_pais_b += (valor_populacao_pais_b * (valor_taxa_crescimento_b /100))
        anos += 1
        
    print(f"{anos} anos")
    while True:
        continuar = input("Deseja continuar? [S]im ou [N]ão: ").upper().strip()
        if continuar == "":
            print("Precisa digitar algo")
            continue
        if continuar[0] == "S":
            break
        elif continuar[0] not in "SN":
            print("Precisa digitar [S] ou [N]")
            continue
        elif continuar[0] == "N":
            CONTINUE = False
            break
            

"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

cidades = []
x = 0
while True:
    codigo_cidade = input(f"Informe o código da {x+1}ª cidade:  ")
    try:
        quantidade_carros = int(input("Quantidade de carros de passeio(em 1999): "))
        if quantidade_carros <= 0:
            print("Precisa digitar um valor acima de 0")
            continue
    except ValueError:
        print("Precisa digitar um valor inteiro")
    try:
        numero_acidentes = int(input("Número de acidentes com vítima(em 1999): "))
        if numero_acidentes < 0:
            print("Precisa ser maior ou igual a 0")
    except ValueError:
        print("Precisa digitar um valor inteiro")
    cidades.append({"Codigo": codigo_cidade, "Quantidade de carros": quantidade_carros, "Numero de acidentes": numero_acidentes})
    x += 1
    if x == 5:
        break
print(cidades)

maior_indice = menor_indice = cidades[0]["Numero de acidentes"]
cidade_maior_indice = cidade_menor_indice = None

for indice in cidades:
    if indice["Numero de acidentes"] > maior_indice:
        maior_indice = indice["Numero de acidentes"]
        cidade_maior_indice = indice["Codigo"]
        
    elif indice["Numero de acidentes"] < menor_indice:
        menor_indice = indice["Numero de acidentes"]
        cidade_menor_indice = indice["Codigo"]
        
media_veiculos = media_acidentes = 0

for m in cidades:
    media_veiculos += m["Quantidade de carros"]
    
for ma in cidades:
    media_acidentes += ma["Numero de acidentes"]
    
print(f"Maior indice de acidentes é da cidade {cidade_maior_indice} com {maior_indice} acidentes")
print(f"Menor indice de acidentes é da cidade {cidade_menor_indice} com {menor_indice} acidentes\n")

print(f"A média de veiculos das 5 cidades: {media_veiculos/5}\n")

print(f"A média de acidentes das 5 cidades: {media_acidentes/x}")

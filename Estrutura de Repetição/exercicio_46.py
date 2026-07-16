# Exercício 46

"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
e depois informe a média dos saltos conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, 
portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m

"""

atletas = []
saltos = 1
nomes_saltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

while True:
    atleta = input("Informe o nome do atleta: ")
    if atleta:
        atletas.append({atleta:[]})
    if not atleta:
        break
    

    while saltos <=5:
        try:
            salto = float(input(f"Informe o {saltos}º salto: "))
            if salto <= 0:
                print("Valor do salto precisa ser maior que 0")
                continue
            atletas[-1][atleta].append(salto)
            saltos += 1
        except ValueError:
            print("Precisa digitar um valor númerico")
            continue
    saltos = 1

for atleta in atletas:
    for nome, lista_saltos in atleta.items():
        print(f"\nAtleta: {nome}")
        
        for i,salto in enumerate(lista_saltos):
            print(f"{nomes_saltos[i]} salto: {salto:.1f}m")
            
        melhor_salto = max(lista_saltos)
        pior_salto = min(lista_saltos)
        
        soma_sem_extremos = sum(lista_saltos) - melhor_salto - pior_salto
        media = soma_sem_extremos / 3
        print(f"\nMelhor salto: {melhor_salto:.1f} m")
        print(f"Pior salto: {pior_salto:.1f} m")
        print(f"Média dos demais saltos: {media:.1f}")
        
        print(f"\nResultado final:")
        print(f"{nome}: {media:.1f} m")

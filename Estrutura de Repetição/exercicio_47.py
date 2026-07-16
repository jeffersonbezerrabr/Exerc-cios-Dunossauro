"""Exercício 47

Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados 
alcançadas pelo atleta em sua apresentação e depois informe a sua média, 
conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informados ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

atletas = []

while True:
    atleta = input("Informe o nome do atleta: ")
    if atleta:
        atletas.append({atleta:[]})
    else:
        break
    
    notas = 1
    
    while notas <= 7:
        try:
            nota = float(input(f"Informe a {notas}ª nota: "))
            if nota < 0:
                print("Nota precisa ser positiva")
                continue
            atletas[-1][atleta].append(nota)
            notas += 1
        except ValueError:
            print("Nota precisa ser um valor númerico!")
            
for a in atletas:
    for nome, lista_notas in a.items():
        print(f"\nAtleta: {nome}")
        
        for nota in lista_notas:
            print(f"    nota: {nota}")
            
        maior_nota = max(lista_notas)
        menor_nota = min(lista_notas)
        
        total_sem_extremos = sum(lista_notas) - maior_nota - menor_nota
        media = total_sem_extremos / 5
        
        print(f"\nMaior nota: {maior_nota}")
        print(f"Menor nota: {menor_nota}")
        print(f"Média: {media}")
        
        print(f"\nResultado final:")
        print(f"{nome}: {media:.1f}")
        print("-" * 30)

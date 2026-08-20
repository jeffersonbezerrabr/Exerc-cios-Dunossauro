# Exercício 06

# Faça um programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.

alunos = {}
media = {}


while len(alunos) < 10:
    aluno = input(f"Informe o nome do {len(alunos)+1}º aluno: ")
    alunos[aluno] = []
    notas = []
    
    while len(notas) < 4:
        try:
            nota = float(input(f"Informe a {len(notas)+1}ª nota: "))
            if nota < 0:
                print("Nota precisa ser maior que 0.")
                continue
            elif nota > 10:
                print("Nota não pode ser maior que 10")
                continue
            else:
                notas.append(nota)
    
        except ValueError:
            print("Precisa digitar um valor númerico!")
            continue
        
    alunos[aluno] = notas
    media[aluno] = sum(notas) / len(notas)
        
na_media = sum(1 for nota in media.values() if nota >= 7)

if na_media:
    print(f"\nQuantidade de alunos na média: {na_media}\n")
    for a,n in media.items():
        if n >= 7:
            print(f"Aluno {a} ficou com nota {n:2.1f}")
else:
     print("\nNenhum aluno ficou na média.")


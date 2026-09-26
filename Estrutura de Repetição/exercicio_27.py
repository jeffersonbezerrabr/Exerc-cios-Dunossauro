# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.

while True:
    try:
        turmas = int(input("Digite quantas turmas são: "))
        if turmas < 1:
            print("Precisa ter ao menos 1 turma!")
        else:
            break
    except ValueError:
        print("Precisa digitar um número inteiro de turmas!")

c = 0
total_alunos = 0

while c < turmas:
    try:
        alunos = int(input(f"Quantos alunos na turma {c + 1}: "))

        if alunos < 1:
            print("Precisa digitar um valor maior que zero")
        elif alunos > 40:
            print("Não pode ter mais de 40 alunos por turma!")
        else:
            total_alunos += alunos
            c += 1

    except ValueError:
        print("Precisa digitar um número inteiro de alunos!")

media = total_alunos / turmas
print(f"A média de alunos por turma é: {media:.2f}")




        


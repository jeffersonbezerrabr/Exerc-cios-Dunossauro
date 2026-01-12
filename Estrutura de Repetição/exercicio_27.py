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
while True:
    alunos = int(input(f"Quantos alunos na turma {c + 1}: "))
    if not alunos:
        print("Precisa digitar algum valor")
    elif alunos > 40:
        print("Não pode ter mais de 40 alunos por turma!")
    elif not int(alunos):
        print("Precisa digitar um número inteiro de alunos!")
    else:
        total_alunos += alunos
        c += 1
    if c == turmas:
        break

media = total_alunos / turmas
print(f"A média de aluno é: {media}")
    


        


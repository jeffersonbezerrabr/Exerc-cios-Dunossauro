"""Exercício 45

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova 
e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:

    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.
"""

"""
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

"""

gabarito = {}
alunos = {}
ALTERNATIVAS = "ABCDE"
notas_alunos = {}
q = 1
CADASTRAR_ALUNO = True

while q <= 10:
    questoes = input(f"Informe a Alternativa da questão {q:.1f}: ").upper()
    if questoes not in ALTERNATIVAS:
        print("Precisa digitar alternativas de A a E")
        continue
    gabarito[q] = questoes
    q += 1

respostas_gabarito = list(gabarito.values())
            
a = 1
c = 1

while CADASTRAR_ALUNO:
    aluno = input(f"Informe o nome do {a}º aluno(a): ").title()
    if aluno == "Fim":
        break
    alunos[aluno] = []
    while c <= 10:
        resposta = input(f"Informe a resposta da {c}ª questão: ").upper()
        if resposta not in ALTERNATIVAS:
            print("Precisa digitar alternativas de A a E")
            continue
        alunos[aluno].append(resposta)
        c += 1
        
    notas_alunos[aluno] = 0
    for cc in range(10):
        if respostas_gabarito[cc] == alunos[aluno][cc]:
            notas_alunos[aluno] += 1
            
    while True:
        continuar = input("Deseja inserir um novo aluno? [S]im ou [N]ão? ").upper().split()
        if continuar[0] == "S":
            break
        
        if continuar[0] not in ["S","N"]:
            print("Precisa digitar [S] ou [N]")
            continue
        
        if continuar[0] == "N":
            CADASTRAR_ALUNO = False
            break
    
    c = 1
    a += 1
    

if notas_alunos:
    print(f"A maior nota foi: {max(notas_alunos.values())}\n")
    print(f"A menor nota foi: {min(notas_alunos.values())}\n")
    print(f"Quantidade de alunos participantes: {len(alunos)}\n")
    print(f"A média das notas foi: {sum(notas_alunos.values()) / len(alunos)}\n")
    
print("Gabarito da prova: ")
for questao, resposta in gabarito.items():
    print(f"Questão {questao}: {resposta}")

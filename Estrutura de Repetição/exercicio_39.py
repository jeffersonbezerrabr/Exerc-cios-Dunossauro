# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
# e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

alunos = []

x = 0

while x < 10:
    try:
        codigo = int(input("Informe seu código: "))
    except ValueError:
        print("O código precisa ser um valor inteiro")
        continue
    try:
        altura = float(input("Infome sua altura: "))
    except ValueError:
        print("Digite um valor válido!")
        continue
    alunos.append({"codigo": codigo, "altura": altura})
    print("Registro realizado!")
    x += 1

if alunos:
    
    maior_altura = menor_altura = alunos[0]["altura"]
    cod_maior_altura = cod_menor_altura = alunos[0]["codigo"]
        
    for aluno in alunos:
        if aluno["altura"] > maior_altura:
            maior_altura = aluno["altura"]
            cod_maior_altura = aluno["codigo"]
        
        elif aluno["altura"] < menor_altura:
            menor_altura = aluno["altura"]
            cod_menor_altura = aluno["codigo"]
    
    
    print(f"Aluno com maior altura: Código - {cod_maior_altura} com altura de {maior_altura}")
    print(f"Aluno com menor altura: Código - {cod_menor_altura} com altura de {menor_altura}")
else:
    print("Nenhum aluno cadastrado!")
# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero         E

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

lista = []

while True:
    n1 = input("Digite a primeira nota: ")
    try:
        nota1 = float(n1)
        lista.append(nota1)
    except ValueError:
        print("Precisa digitar um valor númerico.")
        continue
    n2 = input("Digite a segunda nota: ")
    try:
        nota2 = float(n2)    
        lista.append(nota2)
        break
    except ValueError:
        print("Precisa digitar um valor númerico.")
        continue

media = sum(lista) / len(lista)

if 9 <= media <= 10:
    conceito = "A"
    
elif 7.5 <= media < 9:
    conceito = "B"
    
elif 6 <= media < 7.5:
    conceito = "C"
    
elif 4 <= media < 6:
    conceito = "D"
    
elif media < 4:
    conceito = "E"
    
if conceito in ["A","B","C"]:
    mensagem = "APROVADO"
else:
    mensagem = "REPROVADO"
    
print(f"\nPrimeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
print(f"Situação: {mensagem}")
    
# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:

#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.

notas = []
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

notas.append(nota_1)
notas.append(nota_2)

media = sum(notas) / len(notas)

if media >= 7 and media < 10 :
    print("Aprovado")
    
elif media < 7:
    print("Reprovado")
    
elif media == 10:
    print("Aprovado com Distinção")
    

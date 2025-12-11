# Faça um programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:


    # A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    # A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    # A mensagem "Aprovado com Distinção", se a média for igual a 10.
    
notas = []
x = 1

while x < 4:
    n = input(f"Digite a {x}ª nota: ")
    try:
        if float(n):
            notas.append(float(n))
            x += 1
    except ValueError:
            print("Precisa digitar um valor númerico")
        
media = sum(notas) / len(notas)

if media == 10:
    print(f"Aprovado com Distinção - Média: {media:.2f}")

elif media >= 7:
    print(f"Aprovado - Média {media:.2f}")

else:
    print(f"Reprovado - Média: {media:.2f}")
    


# Faça um programa que calcule o mostre a média aritmética de N notas.

while True:
    try:
        q_notas = int(input("Quantas notas deseja inserir: "))
        if q_notas < 1:
            print("Valor minimo esperado é 1")
        else:
            notas = []
            try:
                for c in range(1, q_notas + 1):
                    nota = float(input(f"Digite a {c}º nota: "))
                    if nota < 0:
                        print("Precisa digitar um valor positivo")
                        break
                    notas.append(nota)
                if len(notas) == q_notas:
                    break
                    
            except ValueError:
                    print("Precisa digitar um valor númerico")
    except ValueError:
        print("Precisa digitar um número inteiro")
        
media = sum(notas) / len(notas)

print(f"A média é : {media}")
                    
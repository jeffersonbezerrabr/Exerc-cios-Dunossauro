# Faça um programa que peça para n pessoas a sua idade, 
# o final o programa devera verificar se a média de idade da turma varia entre
# 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

Continuar = True
idades = []
while Continuar:
    
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 1:
            print("Precisa digitar uma idade valida.")
            continue
        
        idades.append(idade)

        while True:
                sair = input("Deseja sair? [S]im ou [N]ão: ").upper().strip()
                if not sair:
                    print("Precisa digitar algo")
                    continue
                
                if sair[0] == "S":
                    Continuar = False
                    break
                elif sair[0] == "N":
                    break
                elif sair[0] not in "SN":
                    print("Precisa digitar S ou N")
            
    except ValueError:
        print("Precisa digitar um número inteiro")
if idades:
    media = sum(idades) / len(idades)

    if media <= 25:
        turma = "Jovem"
    elif media <= 60:
        turma = "Adulta"
    else:
        turma = "Idosa"
        
    print(f"A turma é {turma}")

else:
    print("Nenhuma idade válida foi informada.")

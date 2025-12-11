#  Exercício 10

# Faça um programa que pergunte em que turno você estuda. Peça para digitar:

#     M - Matutino
#     V - Vespertino
#     N - Noturno.

# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

VALIDADOR = "MVN"

while True:
    turno = input("Informe qual turno deseja estudar: [M]atutino, [V]espertino ou [N]oturno:\n").upper().strip()
    if turno[0] in VALIDADOR:
        if turno[0] == "M":
            print("Bom dia.")
        elif turno[0] == "V":
            print("Boa tarde.")
        elif turno[0] == "N":
            print("Boa noite.")
        break
    
    else:
        print("Opção invalida")

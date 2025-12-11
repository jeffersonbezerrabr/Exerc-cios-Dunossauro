# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"""
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
"""

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

s = 0

while True:
    q01 = input("\nTelefonou para a vítima? [S]im ou [N]ão: ").lower()
    if q01[0] not in "sn":
        print("Precisa responder S]im ou [N]ão:")
        continue
    else:
        if q01[0] == "s":
            s += 1
        break
    
while True:
    q02 = input("\nEsteve no local do crime? [S]im ou [N]ão: ").lower()
    if q02[0] not in "sn":
        print("Precisa responder S]im ou [N]ão:")
        continue
    else:
        if q02[0] == "s":
            s += 1
        break

while True:
    q03 = input("\nMora perto da vítima? [S]im ou [N]ão: ").lower()
    if q03[0] not in "sn":
        print("Precisa responder S]im ou [N]ão:")
        continue
    else:
        if q03[0] == "s":
            s += 1
        break
    
while True:
    q04 = input("\nDevia para a vítima? [S]im ou [N]ão: ").lower()
    if q04[0] not in "sn":
        print("Precisa responder S]im ou [N]ão:")
        continue
    else:
        if q04[0] == "s":
            s += 1
        break
    
while True:
    q05 = input("\nJá trabalhou com a vítima? [S]im ou [N]ão: ").lower()
    if q05[0] not in "sn":
        print("Precisa responder S]im ou [N]ão:")
        continue
    else:
        if q05[0] == "s":
            s += 1
        break

if s == 5:
    classificacao = "Assassino"
    
elif s == 2:
    classificacao = "Suspeita"
    
elif 2 < s < 5:
    classificacao = "Cumplice"
    
else:
    classificacao = "Inocente"

print(f"Baseado nas suas respostas você foi considerado {classificacao}!")

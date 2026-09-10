# Exercício 14

"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
"""

perguntas = {
    "Telefonou para a vítima?" : "",
    "Esteve no local do crime?" : "",
    "Mora perto da vítima?" : "",
    "Devia para a vítima?" : "",
    "Já trabalhou com a vítima?" : "",
}

x = 0
print("Responda [S]im ou [N]ão:\n")

for p in perguntas:
    while True:
        q = input(f"{p} ").strip().lower()
        if q and q[0] in "sn":
            perguntas[p] = "Sim" if q[0] == "s" else "Não"
            break

        print("Por favor, digite apenas 'S' ou 'N'.\n")

resultado = sum(1 for p in perguntas.values() if p == "Sim")

if resultado == 2:
    classificada = "Suspeito"

elif resultado >= 3:
    classificada = "Cúmplice"

elif resultado == 5:
    classificada = "Assassino"

else:
    classificada = "Inocente"

print("\nRespostas registradas:")

print(f"Para {resultado} perguntas, a resposta foi sim. Você é {classificada}!!")

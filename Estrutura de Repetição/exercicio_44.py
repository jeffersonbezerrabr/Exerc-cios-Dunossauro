# Em uma eleição presidencial existem quatro candidatos. 
# Os votos são informados por meio de código. 
# Os códigos utilizados são:

"""
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
0 - Finalizar

Faça um programa que calcule e mostre:

    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A porcentagem de votos nulos sobre o total de votos;
    A porcentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

"""

opcoes = {
    1: ["Jose", 0],
    2: ["João", 0],
    3: ["Maria", 0],
    4: ["Moises", 0],
    5: ["Nulo", 0],
    6: ["Branco", 0],
}

while True:
    print("""
Opções disponiveis:

1 - Jose
2 - João
3 - Maria
4 - Moises
5 - Nulo
6 - Branco
0 - Finalizar
""")
    try:
        escolha = int(input("Digite uma das opções acima: "))
        if escolha < 0 or escolha > 6:
            print("Opção invalida! Digite uma das opções disponíveis\n")
            continue
        elif escolha == 0:
            break
        opcoes[escolha][1] += 1
        
    except ValueError:
        print("Opção invalida! Precisa digitar um valor inteiro de 0 a 6")
        continue
    
print("Votos por candidato:\n")

for codigo in range(1, 5):
    print(
        f"Candidato(a) {opcoes[codigo][0]} "
        f"teve {opcoes[codigo][1]} voto(s)"
    )
        
votos_nulos = opcoes[5][1]
votos_brancos = opcoes[6][1]

print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos brancos: {votos_brancos}")

total = 0

for t in opcoes.values():
    total += t[1]
    
if total > 0:
    porcentagem_nulos = (votos_nulos / total) * 100
    porcentagem_brancos = (votos_brancos / total) * 100
    print(f"A porcentagem de votos nulos sobre o total de votos: {porcentagem_nulos:5.2f}%")
    print(f"A porcentagem de votos em branco sobre o total de votos: {porcentagem_brancos:5.2f}%")
else:
    print("Porcentagem de votos nulos: 0.00%")
    print("Porcentagem de votos brancos: 0.00%")



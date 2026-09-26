# Exercício 04

# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = "aeiou"
consoantes = []
lista = []

while len(lista) < 10:
    texto = input(f"Digite o {len(lista) + 1}º caractere: ").lower().strip()
    
    if not texto:
        print("Entrada inválida. Digite pelo menos um caractere.")
        continue
    elif not texto.isalpha():
        print("Entrada inválida 2. Digite pelo menos um caractere.")
        continue
    
    letra = texto[0]
    lista.append(letra)
    
    if letra.isalpha() and letra not in vogais:
        consoantes.append(letra)


print(f"\nTotal de consoantes lidas: {len(consoantes)}")


if consoantes:
    print("Consoantes lidas:", ", ".join(consoantes))
else:
    print("Nenhuma consoante foi lida.")

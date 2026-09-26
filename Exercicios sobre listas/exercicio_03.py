# Exercício 03

# Faça um programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

while len(notas) < 4:
    try:
        nota = float(input(f"Informe a {len(notas) + 1}ª nota: "))
        if nota < 0:
            print("Nota precisa ser maior ou igual a zero!")
            continue
        else:
            notas.append(nota)
    
    except ValueError:
        print("Precisa digitar um valor númerico!")
        continue
    
media = sum(notas) / len(notas)

for n,c in enumerate(notas):
    print(f"{n + 1}º Nota: {c:5.1f}")

print(f"\nMédia: {media:5.1f}")
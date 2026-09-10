# Exercício 15

"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;


"""

notas = []

while True:
    try:
        nota = float(input(f"Informe a {len(notas) + 1}ª nota: "))
        if nota == -1:
            break
        else:
            notas.append(nota)
    except ValueError:
        print("Precisa digitar um número")
        continue

print("\n\nResultados:\n\n")

print(f"Quantidade de notas inseridas: {len(notas)}\n")

print(f"Notas na ordem que foram inseridas: {notas}\n")

print("Notas na ordem inversa uma abaixa da outra:\n")
for n in notas[::-1]:
    print(n)
    
print(f"\nA soma das notas é: {sum(notas)}")

print(f"\nA média das notas é: {sum(notas) / len(notas)}")

acima_media = [n for n in notas if n > sum(notas) / len(notas)]
print(f"\nA quantidade de notas acima da média é: {len(acima_media)}\nSegue as notas: {acima_media}")

abaixo_de_sete = [n for n in notas if n < 7]
print(f"\nA quantidade de notas abaixo de 7 é: {len(abaixo_de_sete)}\nSegue as notas: {abaixo_de_sete}\n")

mensagem = "Obrigado por testar meu código"

print(mensagem.center(50, "="))
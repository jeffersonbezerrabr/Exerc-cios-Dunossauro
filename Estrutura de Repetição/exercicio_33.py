# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
# que leia as um conjunto indeterminado de temperaturas, e informe ao final 
# a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []

ENCERRAR = False

while not ENCERRAR:
    temp = input("Informe a temperatura para registrar ou [S] para sair: ")
    if temp == "":
        print("Precisa digitar algo")
    elif temp[0].lower() == "s":
        ENCERRAR = True
    else:
        try:
            f_temp = float(temp)
            temperaturas.append(f_temp)
            print("Temperatura registrada com sucesso!\n")
        except ValueError:
            print("Digite uma temperatura ou s para sair!")

if len(temperaturas) > 0:
    maior = max(temperaturas)
    menor = min(temperaturas)
    media = sum(temperaturas) / len(temperaturas)

    print(f"Maior: {maior:.2f}")
    print(f"Menor: {menor:.2f}")
    print(f"Média: {media:.2f}")

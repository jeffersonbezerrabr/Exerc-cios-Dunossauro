# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

    # F - Feminino
    # M - Masculino
    # Sexo Inválido.

while True:
    palavra = input("Digite seu sexo: [F] ou [M]\n").upper().strip()
    if palavra[0] == "F" or palavra[0] == "M":
        break
    else:
        print("Sexo invalido.\n")
        
if palavra[0] == "F":
    print("F - Feminino")
    
elif palavra[0] == "M":
    print("M - Masculino")

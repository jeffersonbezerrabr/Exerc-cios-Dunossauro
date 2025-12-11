# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").lower().strip()

if len(letra) != 1:
    print("Digite apenas uma letra")

else:
    if letra.isdigit():
        print("Você digitou um número")
    elif letra.isalpha():
        if letra in "aeiou":
            print("Você digitou uma vogal")
        else:
            print("Você digitou uma consoante")
    else:
        print("Você digitou um caractere especial")
    


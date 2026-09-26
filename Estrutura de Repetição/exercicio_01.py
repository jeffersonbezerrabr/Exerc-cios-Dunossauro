# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = input("Informe uma nota entre 0 e 10: ")
    
    try:
        f_nota = float(nota)
        print(f"A nota inserida foi {f_nota}.")
        if f_nota < 0:
            print("A nota precisa ser maior/igual a 0")
        elif f_nota > 10:
            print(f"A nota precisa ser menor/igual a 10")
        else:
            print("Nota valida. Está entre 0 e 10. ")
            print("Obrigado!")
            break
    except ValueError:
        print("Precisa digitar um número válido!")
    

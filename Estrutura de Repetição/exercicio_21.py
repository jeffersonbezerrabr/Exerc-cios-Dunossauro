# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

while True:
    n = input("Digite um número: ")
    try:
        int_n = int(n)
        if int_n <= 1:
            print("Ele não é primo")
        
        else:
            primo = True
            for c in range(2, int_n):
                if int_n % c == 0:
                    primo = False
                    break
            
            if primo:
                print(f"{int_n} é primo")
            else:
                print(f"{int_n} não é primo")
        break

    except ValueError:
        print("Precisa digitar um número!")

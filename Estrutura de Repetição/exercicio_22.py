# Altere o programa de cálculo dos números primos, informando, 
# caso o número não seja primo, por quais número ele é divisível.

divisores = []

try:
    n = int(input("Digite um número: "))
    if n < 1:
        print("Ele não é primo")
    elif n == 1:
        print("1 não é primo por definição matemática.")
    else:
        primo = True
        for c in range(2, n):
            if n % c == 0:
                primo = False
                divisores.append(c)
                
        if primo:
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo e é divisível por: {divisores}")
except ValueError:
    print("Precisa digitar um número")
                
    
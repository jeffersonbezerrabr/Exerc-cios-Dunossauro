# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

n = input("Digite um número inteiro para verificar se ele é primo: ")

try:
    int_n = int(n)
    
    if int_n < 2:
        print("Não é primo")
    else:
        eh_primo = True
        for c in range(2, (int_n // 2) + 1):
            if int_n % c == 0:
                eh_primo = False
                break
        
        if eh_primo:
            print("É primo!")
        else:
            print("Não é primo!")

except ValueError:
    print("Precisa digitar um valor inteiro")
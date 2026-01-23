# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5 5! = 5 . 4 . 3 . 2 . 1 = 120

while True:
    try:
        n = int(input("Informe o número para ver seu fatorial: "))
        if n == 0:
            print(f"Fatorial de: {n} é 1")
            break
        elif n > 0:
            print(f"Fatorial de {n}: {n}! =",end=" ")
            for c in range(n,0,-1):
                if c == 1:
                    print(f"{c} = ",end='')
                    break
                print(f"{c} x ",end='')
                
            total = n
            
            for d in range(1, n):
                total *= d
        print(f"{total}")
        exit()
    except ValueError:
        print("Precisa digitar um número.")
                
        
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular 
# o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    n = input("Informe um número inteiro para ver seu fatorial: ")
    try:
        int_n = int(n)
        if int_n < 0:
            print("Precisa ser um número positivo")
            continue
        elif int_n > 16:
            print("Precisa ser menor que 16")
            continue
        elif int_n:
            soma = 1
            for c in range(1, int_n + 1):
                soma *= c
            print(soma)
    except ValueError:
        print("Precisa digitar um número inteiro")
        continue
    
    while True:
        encerrar = input("Deseja encerrar? [S]im ou [N]ão: ").strip().lower()
        
        if encerrar.startswith("n"):
            break  
        
        elif encerrar.startswith("s"):
            print("Programa encerrado.")
            exit()
        
        else:
            print("Resposta inválida. Digite S ou N.")

        
            
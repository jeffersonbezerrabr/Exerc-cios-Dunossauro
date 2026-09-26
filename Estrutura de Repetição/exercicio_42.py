# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
# [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

valores = []
while True:
    try:
        n = int(input("Digite um número inteiro positivo(0 a 100): [Negativo para encerrar]: "))
        if n < 0:
            break
        if n >= 0 and n <= 100:
            valores.append(n)
            if n >= 0 and n <= 25:
                print("Intervalo [0 - 25]")
            
            elif n >= 26 and n <= 50:
                print("Intervalo [26 - 50]")
                
            elif n >= 51 and n <= 75:
                print("Intervalo [51 - 75]")
                
            elif n >= 76 and n <= 100:
                print("Intervalo [76 - 100]")
            
        else:
            print("Valor fora do intervalo permitido (0-100). Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        
print(f"Números digitados: {valores}")
                
                
                
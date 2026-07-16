"""
Exercício 48

Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

Exemplo:

  12376489
  => 98467321

"""

while True:
    try:
        n = int(input("Informe um número inteiro positivo: "))
        if n <= 0:
            print("O valor precisa ser positivo")
            continue
        
        texto_invertido = str(n)[::-1]
        
        for c in texto_invertido:
            print(int(c), end="")
        print()
        break
                
    except ValueError:
        print("Valor precisa ser inteiro!")


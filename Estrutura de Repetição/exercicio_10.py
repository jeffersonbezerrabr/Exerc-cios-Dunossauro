# Faça um programa que receba dois números inteiros e gere os números inteiros 
# que estão no intervalo compreendido por eles.

while True:
    x = input("Digite um número inteiro: ").strip()
    try:
        int_x = int(x)
        break
    except ValueError:
        print("Precisa digitar um número inteiro")
        
while True:
    y = input("Digite outro inteiro: ").strip()
    try:
        int_y = int(y)
        break
    except ValueError:
        print("Precisa digitar um número inteiro")
        
inicio = min(int_x, int_y) + 1
fim = max(int_x, int_y)

for c in range(inicio, fim):
    print(c)
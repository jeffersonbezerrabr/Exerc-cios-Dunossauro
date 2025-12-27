# Altere o programa anterior para mostrar no final a soma dos números.

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

soma = 0

print(f"Numeros no intervalo entre {x} e {y}:")
for c in range(inicio, fim):
    print(c, end=', ')
    soma += c
    
print(f"\nSoma dos números: {soma}")
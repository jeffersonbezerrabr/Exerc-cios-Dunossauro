# Exercício 08

# Faça um programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

while len(idades) < 5 and len(alturas) < 5:
    try:
        i = int(input(f"Informe a idade da {len(idades)+1}ª pessoa: "))
        if i < 0 or i > 150:
            print("Informe uma idade válida")
            continue
        
    except ValueError:
        print("Precisa digitar um valor inteiro")
        continue
    
    try:
       a = float(input(f"Informe a altura da {len(alturas)+1}ª pessoa em metros: "))
       if a < 0:
           print("Informe uma altura válida")
           continue
    except ValueError:
            print("Precisa digitar um valor em metros!")
            continue
    idades.append(i)
    alturas.append(a)
    
# Usando fatiamento (slice) de forma direta
idades_reverso = idades[::-1]
alturas_reverso = alturas[::-1]

# List comprehension com slice 

# idades_reverso = [idades[x] for x in range(len(idades)-1, -1, -1)]
# alturas_reverso = [alturas[y] for y in range(len(alturas)-1, -1, -1)]

# Usando a função reversed:

# idades_reverso = [x for x in reversed(idades)]
# alturas_reverso = [y for y in reversed(alturas)]

print(f"Idades ao contario: {idades_reverso}")
print(f"Alturas ao contario: {alturas_reverso}")

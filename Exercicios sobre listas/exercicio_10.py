# Exercício 10

# Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = []
lista2 = []

while len(lista1) < 10 and len(lista2) < 10:
    n1 = input(f"Informe o {len(lista1)+ 1}º elemento da primeira lista: ")
    if not n1:
        print("Precisa digitar algo.")
        continue
    
    n2 = input(f"Informe o {len(lista2)+ 1}º elemento da segunda lista: ")
    if not n2:
        print("Precisa digitar algo.")
        continue
    
    lista1.append(n1)
    lista2.append(n2)
    
lista3 = []

for par in zip(lista1, lista2): # 1. Percorre cada par gerado pelo zip
    for item in par: # 2. Percorre cada elemento individual de dentro daquele par
        lista3.append(item) # 3. Adiciona o elemento na lista final

print(lista3)

        
        
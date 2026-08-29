# Exercício 11

# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.


lista1 = []
lista2 = []
lista3 = []
lista4 = []


while len(lista1) < 10 and len(lista2) < 10 and len(lista3) < 10:
    n1 = input(f"Informe o {len(lista1)+ 1}º elemento da primeira lista: ")
    if not n1:
        print("Precisa digitar algo.")
        continue
    
    n2 = input(f"Informe o {len(lista2)+ 1}º elemento da segunda lista: ")
    if not n2:
        print("Precisa digitar algo.")
        continue
    
    n3 = input(f"Informe o {len(lista3)+ 1}º elemento da terceira lista: ")
    if not n3:
        print("Precisa digitar algo.")
        continue
    
    lista1.append(n1)
    lista2.append(n2)
    lista3.append(n3)
    
for a,b,c in zip(lista1,lista2,lista3):
    lista4.append(a)
    lista4.append(b)
    lista4.append(c)
    
print(*lista4, sep=' - ')
    

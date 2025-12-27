# Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.

lista = []

while True:
    n = input("Informe um número: ")
    try:
        int_n = int(n)
        
        if not lista:
            maior = menor = int_n
        else:
            if int_n > maior:
                maior = int_n
            elif int_n < menor:
                menor = int_n
                
        lista.append(int_n)
        
    except ValueError:
        print("Precisa digitar um número inteiro")
        continue
    
    sair = input("Deseja parar? [S]im ou [N]ão: ").lower().strip()
    
    if not sair:
        print("Precisa digitar S ou N")
        lista.pop()
        continue
    
    if sair[0] == "n":
        continue
    
    elif sair[0] == "s":
        break
    else:
        print("precisa digitar S ou N")
        lista.pop()
print(f"O maior número digitado: {maior}")
print(f"O menor número digitado: {menor}")
print(f"Soma dos valores: {sum(lista)}")
print(lista)

# Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

#     326 = 3 centenas, 2 dezenas e 6 unidades

#     12 = 1 dezena e 2 unidades

# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

v = input("Digite um número entre 1 e 999: ")

qntd = len(v)

if qntd > 3:
    print("O valor maximo: 999")

elif qntd == 3:
    if int(v[0]) > 1 and int(v[1]) > 1 and int(v[2]) > 1:
        print(f"{v[0]} Centenas, {v[1]} dezenas e {v[2]} unidades")
        
    elif int(v[0]) > 1 and int(v[1]) > 1 and int(v[2]) == 1:
        print(f"{v[0]} Centenas, {v[1]} dezenas e {v[2]} unidade")
        
    elif int(v[0]) > 1 and int(v[1]) <= 1 and int(v[2]) <= 1:
        print(f"{v[0]} Centenas, {v[1]} dezena e {v[2]} unidade")
        
    elif int(v[0]) > 1 and int(v[1]) > 1 and int(v[2]) <= 1:
        print(f"{v[0]} Centenas, {v[1]} dezenas e {v[2]} unidade")
        
    elif int(v[0]) > 1 and int(v[1]) <= 1 and int(v[2]) > 1:
        print(f"{v[0]} Centenas, {v[1]} dezena e {v[2]} unidades")
        
    elif int(v[0]) <= 1 and int(v[1]) > 1 and int(v[2]) > 1:
        print(f"{v[0]} Centena, {v[1]} dezenas e {v[2]} unidades")
        
    elif int(v[0]) <= 1 and int(v[1]) > 1 and int(v[2]) <= 1:
        print(f"{v[0]} Centena, {v[1]} dezenas e {v[2]} unidade")
        
    else:
        print(f"{v[0]} Centena, {v[1]} dezena e {v[2]} unidade")

elif qntd == 2:
    if int(v[0]) > 1 and int(v[1]) > 1:
        print(f"{v[0]} Dezenas e {v[1]} unidades")
    
    elif int(v[0]) > 1 and int(v[1]) <= 1:
        print(f"{v[0]} Dezenas e {v[1]} unidade")
        
    elif int(v[0]) <= 1 and int(v[1]) > 1:
        print(f"{v[0]} Dezena e {v[1]} unidades")
    
    else:
        print(f"{v[0]} Dezena e {v[1]} unidade")
        
else:
    if int(v[0]) > 1:
        print(f"{v} Unidades")
    else:
        print(f"{v} Unidade")
        
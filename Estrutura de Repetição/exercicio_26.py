# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato_1 = candidato_2 = candidato_3 = 0

while True:
    try:
        t = int(input("Quantos eleitores vão votar: "))
        if t < 1:
            print("Quantidade de eleitores precisa ser maior que 0!")
            continue
        else:
            print(f"Registrado! Serão {t} eleitores.")
            break
    except ValueError:
        print("Precisa digitar um número inteiro positivo!")
        continue

c = 0

while t != c:
    try:
        voto = int(input(f"Eleitor {c + 1}, digite o número do seu candidato: [1], [2], [3]\n "))
        if voto in [1,2,3]:
            if voto == 1:
                candidato_1 += 1
                print("Voto registrado com sucesso!")
            elif voto == 2:
                candidato_2 +=1
                print("Voto registrado com sucesso!")
                
            elif voto == 3:
                candidato_3 +=1
                print("Voto registrado com sucesso!")
            c += 1
    
        else:
            print("Precisa digitar [1], [2], [3]")
                    
    except ValueError:
        print("Precisa digitar um valor númerico")
    
print(f"""
O candidato 1 recebeu {candidato_1} votos
O candidato 2 recebeu {candidato_2} votos
O candidato 3 recebeu {candidato_3} votos""")
    

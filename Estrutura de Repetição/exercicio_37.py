# Uma academia deseja fazer um censo entre seus clientes para descobrir:
# o mais alto, o mais baixo, a mais gordo e o mais magro, 
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, 
# sua altura e seu peso. O final da digitação de dados deve ser dada quando 
# o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores
# do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes


clientes = []
while True:
    try:
        codigo = int(input("Digite o seu código (0 para sair): "))
        if codigo == 0:
            break
        altura = float(input("Digite a sua altura: "))
        peso = float(input("Digite o seu peso: "))
        # Armazena os dados como outro dicionário dentro do principal
        clientes.append({"codigo": codigo, "altura": altura, "peso": peso})
    except ValueError:
        print("Precisa digitar valores númericos")
    
if clientes:

    maior_peso = menor_peso = clientes[0]["peso"]
    maior_altura = menor_altura = clientes[0]["altura"]

    cod_maior_peso = cod_menor_peso = clientes[0]["codigo"]
    cod_maior_altura = cod_menor_altura = clientes[0]["codigo"]

    for cliente in clientes:
        if cliente["peso"] > maior_peso:
            maior_peso = cliente["peso"]
            cod_maior_peso = cliente["codigo"]
            
        if cliente["peso"] < menor_peso:
            menor_peso = cliente["peso"]
            cod_menor_peso = cliente["codigo"]
        
        if cliente["altura"] > maior_altura:
            maior_altura = cliente["altura"]
            cod_maior_altura = cliente["codigo"]
        
        if cliente["altura"] < menor_altura:
            menor_altura = cliente["altura"]
            cod_menor_altura = cliente["codigo"]
              
    print(f"Cliente do código {cod_maior_peso} possui o maior peso: {maior_peso}Kg\n")
    print(f"Cliente do código {cod_menor_peso} possui o menor peso: {menor_peso}Kg\n")
    print(f"Cliente do código {cod_maior_altura} possui o maior altura: {maior_altura}\n")
    print(f"Cliente do código {cod_menor_altura} possui o menor altura: {menor_altura}\n")

else:
    print("Nenhum cliente cadastrado!")

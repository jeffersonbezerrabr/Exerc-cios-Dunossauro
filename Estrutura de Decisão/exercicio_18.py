# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ").strip()


try:
    if "//" in data:
        print("Data invalida: barras duplas encontradas")
    elif len(data) != 10:
        print("Data invalida! Formato incorreto")
    
    else:
        data_tratada = data.split("/")
        
        if len(data_tratada) != 3:
            print("Data invalida! Formato incorreto")
        else:
            dia = int(data_tratada[0])
            mes = int(data_tratada[1])
            ano = int(data_tratada[2])
            
        
        if mes < 1 or mes > 12:
            print("Data inválida: Mês deve estar entre 01 e 12")
            
        elif dia < 1 or dia > 31:
            print("Data inválida: Dia deve estar entre 01 e 31")
            
        else:
            print("Data Valida")
            
except ValueError:
    print("Erro: certifique-se de digitar apenas números entre as barras")
except IndexError:
    print("Erro: formato incorreto da data")

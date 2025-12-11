# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que 
# faça a conversão para Megabytes, usando a seguinte fórmula:

# Formula

#Gigabytes * 1024

Gb = float(input("Informe o valor em Gb a ser convertido para Mb: "))

Mb = Gb * 1024

print(f'O arquivo tem {Mb} MBs')

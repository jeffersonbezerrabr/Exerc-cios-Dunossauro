# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que 
# faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

#     Para Megabytes: Gigabytes * 1024
#     Para Kilobytes: Gigabytes * 1024 * 1024

# Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes

Gb = float(input("Informe o valor em Gb a ser convertido para Mb e Kb: "))

Mb = Gb * 1024
Kb = Gb * 1024 * 1024

print(f'O arquivo tem {Mb} MBs')
print(f'O arquivo tem {Kb} Kbs')

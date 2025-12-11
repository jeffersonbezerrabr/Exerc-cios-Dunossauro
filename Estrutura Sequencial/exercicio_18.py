# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Informe o tamanho do arquivo em MB: "))
internet = float(input("Informe a velocidade da sua internet em Mbps: "))

velocidade_bits = internet / 8

tempo_segundos = tamanho / velocidade_bits

tempo_minutos = int(tempo_segundos / 60)

print(f"O download do arquivo de {tamanho}MB levará aproximadamente {tempo_minutos} minutos para baixar.")

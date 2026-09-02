# Exercício 13
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).

meses = {
    "Janeiro": 0,
    "Fevereiro": 0,
    "Março": 0,
    "Abril": 0,
    "Maio": 0,
    "Junho": 0,
    "Julho": 0,
    "Agosto": 0,
    "Setembro": 0,
    "Outubro": 0,
    "Novembro": 0,
    "Dezembro": 0,
}

for mes in meses:
    while True:
        try:
            temperatura = float(input(f"Informe a média da temperatura do mês de {mes}: "))
            meses[mes] = temperatura
            break
        except ValueError:
            print("Valor precisa ser numérico. Tente novamente.")

soma = 0

for c,v in meses.items():
    soma += v
    
media = soma / len(meses)
x = 1

for c,v in meses.items():
    if v >= media:
        print(f"{x} - {c} - média: {v}º C")
        x += 1
        

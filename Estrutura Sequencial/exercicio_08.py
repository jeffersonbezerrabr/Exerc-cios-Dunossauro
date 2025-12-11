# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Quanto você ganha por hora: "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês: "))

salario_mes = valor_hora * horas_trabalhadas

print(f"O seu salário por mês é, R$ {salario_mes}")

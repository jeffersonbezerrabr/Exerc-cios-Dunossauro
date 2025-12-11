# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR: 
# - Salário Bruto até 900 (inclusive) - isento 
# - Salário Bruto até 1500 (inclusive) - desconto de 5% 
# - Salário Bruto até 2500 (inclusive) - desconto de 10% 
# - Salário Bruto acima de 2500 - desconto de 20%

# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

"""
Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00
"""

valor_hora = float(input("Informe o valor da sua hora/trabalho: "))
qntd_horas_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * qntd_horas_mes
FGTS = 0.11
INSS = 0.10

if salario_bruto <= 900:
    IR = 0
elif salario_bruto <= 1500:
    IR = 0.05
elif salario_bruto <= 2500:
    IR = 0.10
else:
    IR = 0.20
    
total_descontos = (salario_bruto * IR) + (salario_bruto * INSS)
salario_liquido = salario_bruto - (salario_bruto * IR) - (salario_bruto *INSS)
    
if salario_bruto > 900:
    print(f"""Sálario Bruto: R$: {salario_bruto:.2f}
(-) IR ({IR * 100}%): R$ {salario_bruto * IR:.2f}
(-) INSS ({INSS * 100}%): R$ {salario_bruto * INSS:.2f}
(+) FGTS ({FGTS * 100}%): R$ {salario_bruto * FGTS:.2f}
Total de descontos: R$ {total_descontos:.2f}
Salário Liquido: R$ {salario_liquido:.2f}""")
    
else:
    print(f"""Sálario Bruto: R$: {salario_bruto:.2f}
IR: Isento
(-) INSS ({INSS * 100}%): R$ {salario_bruto * INSS:.2f}
(+) FGTS ({FGTS * 100}%): R$ {salario_bruto * FGTS:.2f}
Total de descontos: R$ {total_descontos:.2f}
Salário Liquido: R$ {salario_liquido:.2f}""")


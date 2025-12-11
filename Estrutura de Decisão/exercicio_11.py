# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes. 
# Faça um programa que recebe o salário de um colaborador 
# e o reajuste segundo o seguinte critério, baseado no salário atual:

#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.


salario_atual = float(input("Informe o seu salario: "))

if salario_atual <= 280:
    percentual = 0.20

    
elif salario_atual > 280 and salario_atual <= 700:
    percentual = 0.15

    
elif salario_atual > 700 and salario_atual <= 1500:
    percentual = 0.10

else:
    percentual = 0.05

aumento = salario_atual * percentual
novo_salario = salario_atual + aumento
    
print(f"""
Salario antes do reajuste: R$ {salario_atual:.2f}
Percentual aplicado: {(percentual * 100):.0f}%
Aumento de: R$ {aumento:.2f}
Novo Salário: R$ {novo_salario:.2f}""")

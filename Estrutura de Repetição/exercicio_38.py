"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""



ano_inicial = 1995
# salario = float(input("Informe o salario inicial: "))
salario = 1000
percentual = 0.015
salario += salario * percentual

print(salario)

for c in range(1997, 2027):
    percentual *= 2
    salario += salario * percentual
    print(f"Salario de {c} é: {salario:,.2f}")

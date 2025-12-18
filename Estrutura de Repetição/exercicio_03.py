# Faça um programa que leia e valide as seguintes informações:

"""
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input("Digite seu nome: ").split()
    if len(nome) <= 3:
        print("Precisa ter mais que 3 caracteres")
        continue
    break

while True:
    idade = input("Digite sua idade: ")
    try:
        idade_int = int(idade)
        if idade_int < 0 or idade_int > 150:
            print("Idade precisa estar entre 0 e 150")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico")
        continue
    break

while True:        
    salario = input("Informe seu salário: ")
    try:
        salario_float = float(salario)
        if salario_float <= 0:
            print("Salario precisa ser maior que zero")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico.")
        continue
    break

while True:
    estado_civil = input("Informe seu estado civil\n"
"Opções disponiveis:\n\n"

"[S]olteiro\n"
"[C]asado\n"
"[V]iuvo\n"
"[D]ivorciado\n"

"Digite a opção: ").upper()
    if estado_civil[0] not in "SCVD":
        print("Precisa digitar [S,C,V,D]")
        continue
    break
print("Obrigado por participar!")

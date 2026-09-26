# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

cadastros = []

print("Cadastro de usuário:\n")

while True:
    login = input("Insira o nome do usuário que deseja cadastrar: ")
    senha = input("Digite uma senha: ")
    if senha == login:
        print("Login e senha não podem ser iguais")
        continue
    cadastro = {
        "usuario": login,
        "senha": senha
    }

    cadastros.append(cadastro)
    break

print("Cadastro realizado com sucesso! Obrigado.")

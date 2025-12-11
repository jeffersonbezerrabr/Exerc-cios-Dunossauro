# # Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

while True:
    a = float(input("Informe o valor de 'a': "))
    if a == 0:
        print("Encerrando! A equação não é do segundo grau")
        break
    else:
        b = float(input("Informe o valor de 'b': "))
        c = float(input("Informe o valor de 'c': "))
        break

Delta = (b ** 2) - (4*a*c)

x1 = (-b + (Delta ** 0.5)) / (2*a)

x2= (-b - (Delta ** 0.5)) / (2*a)

if Delta < 0:
    print("\nDelta negativo! a equação não possui raizes reais. Encerrando...")

elif Delta == 0:
    print(f"\nDelta: {Delta}")
    print("Delta igual a zero! A equação possui apenas uma raiz real")
    print(f"X: {x1}")

else:
    print(f"\nDelta: {Delta}")
    print("Delta Positivo! A equação possui duas raiz reais")
    print(f"X1: {x1}")
    print(f"X2: {x2}")

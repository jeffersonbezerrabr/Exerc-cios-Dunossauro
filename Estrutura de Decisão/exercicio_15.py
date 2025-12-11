# # Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:

#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     Triângulo Equilátero: três lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;

l1 = float(input("Informe um lado: "))
l2 = float(input("Informe mais um lado: "))
l3 = float(input("Informe outro lado: "))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print("É possível formar um triangulo")
    
    if l1 == l2 == l3:
        print("Triângulo Equilátero: três lados iguais")
        
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo Isósceles: quaisquer dois lados iguais")

    else:
        print("Triângulo Escaleno: três lados diferentes")
else:
    print("Não é possível formar um triângulo")

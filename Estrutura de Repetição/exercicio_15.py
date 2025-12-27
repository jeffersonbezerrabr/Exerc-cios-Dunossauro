# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

while True:
    f = input("Informe o valor de F: ")
    try:
        int_f = int(f)
        if int_f >= 0:
            break
        else:
            print("Precisa ser maior ou igual 0")
            continue
    except ValueError:
        print("Precisa digitar um valor númerico")
        continue

a = 0
b = 1

for i in range(int_f):
    print(a)
    novo_a = b
    novo_b = a + b
    a = novo_a
    b = novo_b
    
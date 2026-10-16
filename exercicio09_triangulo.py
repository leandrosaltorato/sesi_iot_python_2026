a = float(input("Digite o comprimento do lado 1: "))
b = float(input("Digite o comprimento do lado 2: "))
c = float(input("Digite o comprimento do lado 3: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Esses comprimentos não formam um triângulo")
elif a == b == c:
    print("Triângulo equilátero")
elif a == b or a == c or b == c:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")

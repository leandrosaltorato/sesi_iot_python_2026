n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("O fatorial só existe para números inteiros positivos (ou zero).")
else:
    fatorial = 1
    for i in range(2, n + 1):
        fatorial = fatorial * i
    print("O fatorial de", n, "é", fatorial)

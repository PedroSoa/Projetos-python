numero = int(input("Digite um número de 1 a 10 para a tabuada: "))

if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Número fora do intervalo válido. Digite um número de 1 a 10.")
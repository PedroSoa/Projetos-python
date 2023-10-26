soma = 0
contagem = 0

while True:
    numero = int(input("Digite um número (0 para encerrar): "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
        soma += numero
        contagem += 1

if contagem == 0:
    print("Nenhum número par foi digitado.")
else:
    media = soma / contagem
    print(f"A média dos números pares digitados é: {media}")

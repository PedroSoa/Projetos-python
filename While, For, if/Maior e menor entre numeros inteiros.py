maior = menor = None

while True:
    numero = int(input("Digite um número (0 para encerrar): "))
    
    if numero == 0:
        break  
    
    if maior is None or menor is None:
        maior = menor = numero
    else:
        
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

if maior != None:
    print(f"O maior número digitado é: {maior}")
    print(f"O menor número digitado é: {menor}")
else:
    print("Nenhum número foi digitado.")


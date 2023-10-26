print("*=================================================================*")
print("*========================= Cálculo do IMC ========================*")
print("*=================================================================*")
print("*                                                                 *")
altura = int(input('*Digite sua altura (em cm): '))
peso = float(input('*Digite seu peso: '))
print("")
while altura <= 0 and peso <= 0:
    print('Peso e altura devem ser maiores que 0')
    print("*=================================================================*")
    altura = int(input('*Digite sua altura (em cm): '))
    peso = float(input('*Digite seu peso: '))
    print("")
    
altura = altura/100
IMC = peso/(altura*altura)
IMC = round(IMC, 2)
if IMC > 16 and IMC < 16.9:
    print(f'Seu IMC é de: {IMC}\nSua classificação é: "Muito abaixo do peso"')
elif IMC > 17 and IMC < 18.5:
    print(f'Seu IMC é de: {IMC}\nSua classificação é: "Abaixo do peso"')
elif IMC > 18.5 and IMC < 24.9:
    print(f'Seu IMC é de: {IMC}\nSua classificação é: "Peso normal"')
elif IMC > 25 and IMC < 29.9:
    print(f'Seu IMC é de: {IMC}\nSua classificação é: "Acima do peso"')
elif IMC > 30 and IMC < 34.9:
    print(f'Seu IMC é de: {IMC}\nSua classificação é: "Obesidade Grau I"')
elif IMC > 35 and IMC < 40:
    print(f'Seu IMC é de: {IMC}\nSua classificação é: "Obesidade Grau II"')
elif IMC > 40:
    print(f'Seu IMC é de: {IMC}\nSua classificação é: "Obesidade Grau III"')

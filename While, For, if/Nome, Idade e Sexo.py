print("*================================================================*")
print("*====================== Nome, Sexo e Idade ======================*")
print("*================================================================*")
print("*                                                                *")
nome = str(input('*Digite seu nome: '))
idade = int(input('*Digite sua idade: '))
while True:
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

    if sexo == "M":
        print("Sexo masculino registrado.")
        break
    elif sexo == "F":
        print("Sexo feminino registrado.")
        break
    else:
        print("Opção inválida. Digite 'M' para masculino ou 'F' para feminino.")
print('')
print(f'Suas informações são: \nNome: {nome}\nIdade: {idade}\nSexo: {sexo}')
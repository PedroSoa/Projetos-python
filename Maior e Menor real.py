Lista = []
maior = 0
menor = 0
for contagem in range(0, 5):
    Lista.append(float(input(f"Digite um valor real para a posição {contagem}: ")))
if contagem == 0:
    maior = menor = Lista[contagem]
else:
    if Lista[contagem] > maior:
        maior = Lista[contagem]
    if Lista[contagem] < menor:
        menor = Lista[contagem]

print("="*30)
print(f"Os valores da lista são: {Lista}")
print(f'O maior valor foi: {max(Lista)}')
for i, v in enumerate(Lista):
    if min(Lista) == v:
        print(f'{i}')
print(f'O menor valor foi: {min(Lista)}')
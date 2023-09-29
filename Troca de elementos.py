A = list()
B = list()
C = A
for contagem in range(0,5):
    A.append(int(input("Digite um valor para lista A: ")))
print("="*40)
for contagem in range(0,5):
    B.append(int(input("Digite um valor para lista B: ")))
print("="*40)
print (f"A lista A é:{A}")
print (f'A lista B é:{B}')
A = C
A = B
print("="*40)
print(f'A nova lista A é:{A}')
print(f'A nova lista B é:{C}')
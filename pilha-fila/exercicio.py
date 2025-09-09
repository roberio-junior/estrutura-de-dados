string = "abelha"
pilha = list(string)
print(pilha)

invertida = ""
while (len(pilha) > 0):
    e = pilha.pop()
    invertida += e
    print(invertida)

print("\nString invertida:",invertida)

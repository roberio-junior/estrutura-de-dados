def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    pilha = []  # guarda operadores e parênteses
    saida = []  # resultado pós-fixa

    for i in expressao:
        if i.isalnum(): # verifica se é uma letra ou número
            saida.append(i)  # operando vai direto pra saída
        elif i == '(':
            # Se for parêntese de abertura, empilha para aguardar fechamento
            pilha.append(i)
        elif i == ')':
            # desempilha até encontrar '('
            while pilha and pilha[-1] != '(':
                saida.append(pilha.pop()) # Adiciona os operadores na saída
            pilha.pop()  # Remove o '(' da pilha (sem adicionar na saída)
        else:
            # Se for operador (+, -, *, /, ^)
            # Enquanto houver operadores na pilha com precedência maior ou igual,
            # desempilha eles para a saída (respeitando associatividade)
            while pilha and pilha[-1] != '(' and precedencia.get(i,0) <= precedencia.get(pilha[-1],0):
                saida.append(pilha.pop())
            pilha.append(i)  # empilha o operador atual

    while pilha:
        saida.append(pilha.pop())  # desempilha tudo que sobrou

    return ' '.join(saida)  # junta e retorna a expressão pós-fixa

# Testes
print(infixa_para_posfixa('A+B'))
print(infixa_para_posfixa('A+B*C'))
print(infixa_para_posfixa('(A+B)*C'))
print(infixa_para_posfixa('A+B*C-D/E'))

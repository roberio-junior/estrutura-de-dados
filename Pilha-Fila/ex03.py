def esta_balanceada(expressao):
    pilha = []  # pilha vazia para armazenar os caracteres de abertura

    # Percorremos cada caractere da expressão
    for caractere in expressao:
        # Se for um símbolo de abertura, empilhamos
        if caractere == '(' or caractere == '[' or caractere == '{':
            pilha.append(caractere)

        # Se for um símbolo de fechamento, verificamos se há um par correspondente
        elif caractere == ')':
            # Se a pilha estiver vazia ou o topo não for o par correspondente, está desbalanceado
            if not pilha or pilha[-1] != '(':
                return False
            pilha.pop()  # Remove o par correspondente do topo da pilha

        elif caractere == ']':
            if not pilha or pilha[-1] != '[':
                return False
            pilha.pop()

        elif caractere == '}':
            if not pilha or pilha[-1] != '{':
                return False
            pilha.pop()

    # Se a pilha estiver vazia ao final, a expressão está balanceada
    if len(pilha) == 0:
        return True
    else:
        return False


# Lista de expressões para testar a função
expressoes = [
    "{[()]}",
    "{[(])}",
    "((()))[]{}",
    "([)]",
    "([{}])()",  
    "(()",
    ")",
    "([]{})",        
    "[({})]",    
]

# Testando cada expressão e imprimindo o resultado
for exp in expressoes:
    print(f"{exp}: {esta_balanceada(exp)}")

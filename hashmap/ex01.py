# Dicionário com nomes como chaves e idades como valores (inteiros)
idades = {"Robério": 21, "Daniel": 30, "João": 19}

# Imprime a idade do Robério
print("A idade de Robério é", idades["Robério"])

# Adiciona uma nova chave "Janeide" com valor 45
idades["Janeide"] = 45

# Remove a chave "João" do dicionário
del idades["João"]

# Tenta obter a idade da "Maria". Como não existe, retorna None
print(idades.get("Maria"))

# Imprime a idade de cada pessoa
for key, value in idades.items():
    print(f"A idade de {key} é {value}")

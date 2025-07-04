# Dicionário com países como chave e suas capitais como valor
pais_capital = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa"
}

# Dicionário vazio para armazenar o mapeamento invertido
capital_pais = {}

# Percorre os pares (país, capital) no dicionário original
for key, value in pais_capital.items():
    # Atribui a capital como chave e o país como valor no novo dicionário
    capital_pais[value] = key

# Imprime o dicionário original
print("Dicionário inicial:")
print(pais_capital)

# Imprime o dicionário invertido
print("Dicionário invertido:")
print(capital_pais)

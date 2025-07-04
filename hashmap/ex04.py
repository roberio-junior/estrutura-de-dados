# Dicionário com produtos e seus preços
produtos = {
    "Arroz": 15.90,
    "Feijão": 7.50,
    "Macarrão": 4.20,
    "Leite": 5.10,
    "Pão": 2.80,
    "Queijo": 55.00,
    "Café Premium": 60.00,
    "Carne Bovina": 75.50
}

# Dicionário vazio para armazenar produtos com preço acima de 50
produtos_caros = {}

# Percorre todos os produtos e preços
for key, value in produtos.items():
    # Se o preço for maior que 50, adiciona ao dicionário produtos_caros
    if value > 50:
        produtos_caros[key] = value

# Exibe os produtos que custam mais de R$ 50,00
print("Produtos com preço acima de R$ 50,0:")
for key, value in produtos_caros.items():
    print(f"{key}: R${value}")

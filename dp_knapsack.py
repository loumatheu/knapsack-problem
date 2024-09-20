class item:
    def __init__(self, id, name, weight, value):
        self.id = id
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"Weight: {self.weight} Value: {self.value}"

    def __repr__(self):
        return (
            f"ID: {self.id} Name:{self.name} Weight: {self.weight} Value: {self.value}"
        )


def knapsack(capacity, items, n):
    # Criando a tabela dp com tamanho (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Preenchendo a tabela
    for i in range(1, n + 1):  # itens (linha)
        for w in range(1, capacity + 1):  # capacidades (coluna)
            # Se o peso do item atual é menor ou igual ao peso limite
            if items[i - 1].weight <= w:
                # Decisão: incluir o item ou não
                dp[i][w] = max(
                    dp[i - 1][w], items[i - 1].value + dp[i - 1][w - items[i - 1].weight]
                )
            else:
                # Caso o item não possa ser incluído
                dp[i][w] = dp[i - 1][w]

            # LOGs
            # print(f"Item atual: {items[i - 1].name}")
            # print(f"i = {i}")
            # print(f"Peso disponível = {w}")
            # print(f"Valores dos itens inclusos = {dp[i][w]}\n")

    print("Matriz Programação Dinâmica:")
    for row in dp:
        print(row)
    # O valor máximo será dp[n][capacity]
    return dp[n][capacity]


# Criação e alocação dos itens na lista de itens
item_1 = item(id=3, name="Pedra", weight=3, value=8)
item_2 = item(id=2, name="Rocha", weight=2, value=3)
item_3 = item(id=4, name="Prata", weight=4, value=9)
item_4 = item(id=1, name="Brita", weight=1, value=6)

items_list = [item_1, item_2, item_3, item_4]

capacity = 5
n = len(items_list)

max_value = knapsack(capacity, items_list, n)
print("O valor máximo que pode ser obtido é:", max_value)

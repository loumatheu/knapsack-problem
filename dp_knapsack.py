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


def knapsack(capacity, weights, values, n):
    # Criando a tabela dp com tamanho (n+1) x (capacity+1) 
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Preenchendo a tabela
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Se o peso do item atual é menor ou igual ao peso limite
            if weights[i - 1] <= w:
                # Decisão: incluir o item ou não
                dp[i][w] = max(
                    dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                # Caso o item não possa ser incluído
                dp[i][w] = dp[i - 1][w]

    # O valor máximo será dp[n][capacity]
    return dp[n][capacity]


item_1 = item(id=1, name="Smartphone", weight="1", value="6")
item_2 = item(id=2, name="Mouse", weight="4", value="9")
item_3 = item(id=3, name="Keyboard", weight="2", value="3")
item_4 = item(id=4, name="Headphones", weight="3", value="8")

items_list = []

for i in range(1, 5):
    items_list.append(globals()[f"item_{i}"])


# Exemplo de uso
values = [8, 3, 9, 6]
weights = [3, 2, 4, 1]
capacity = 5
n = len(values)

max_value = knapsack(capacity, weights, values, n)
print("O valor máximo que pode ser obtido é:", max_value)

dp = [[0 for _ in range(capacity + 1) for _ in range(n + 1)]]

print("Visualizando linhas:")
for linha in dp:
    for elemento in linha:
        print(elemento, end=" ")
    print()

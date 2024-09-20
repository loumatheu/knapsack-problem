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

# Função auxiliar para ordenar os itens pela relação valor/peso
def sort_by_values(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i].value < items[j].value:
                # Trocar de posição se o item j for melhor que o item i
                items[i], items[j] = items[j], items[i]


def greedy_knapsack(capacity, items):
    # Ordenando itens pela maior relação valor/peso
    sort_by_values(items)

    total_value = 0
    total_weight = 0
    solution = []

    for item in items:
        if total_weight + item.weight <= capacity:
            solution.append(item)
            total_value += item.value
            total_weight += item.weight
        else:
            continue

    # Exibindo os itens escolhidos
    print("\nItens escolhidos na solução gulosa:")
    for i in solution:
        print(i)

    return total_value


# Criação e alocação dos itens na lista de itens
item_1 = item(id=3, name="Pedra", weight=3, value=8)
item_2 = item(id=2, name="Rocha", weight=2, value=3)
item_3 = item(id=4, name="Prata", weight=4, value=9)
item_4 = item(id=1, name="Brita", weight=1, value=6)

items_list = [item_1, item_2, item_3, item_4]

capacity = 5

# Chamando a função gulosa
max_value_greedy = greedy_knapsack(capacity, items_list)
print("O valor máximo obtido pela abordagem gulosa é:", max_value_greedy)

# List = Usado para guardar multíplos itens em uma única variável

food = ["pizza","hamburguer","hotdog","spaghetti","pudding"]

food[0] = "sushi"

food.append("ice cream") # Adiciona o item entre () ao final da lista.
food.remove("hotdog") # Remove o item entre () da lista.
food.pop() # Remove o ultimo item da lista.
food.insert(0,"cake") # Adiciona o item entre () na posição dada.
food.sort() # Ordena os itens da lista em ordem alfabética.
food.clear() # Remove todos os itens da lista.

for x in food:
    print(x)
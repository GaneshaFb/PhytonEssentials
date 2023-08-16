# 2D lists = uma lista de listas

drinks = ["coffe","soda","tea"]
dinner = ["pizza","hamburguer","hotdog"]
desert = ["cake","ice cream"]

food = [drinks,dinner,desert]

print(food[1][2])

for i in food:
    for j in i:
        print(j)

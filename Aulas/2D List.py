# 2D List = Uma lista de listas.

drinks = ["coffe","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]

print(food[1][2])

for i in food:
    for j in i:
        print(j)

# Loop Control Statements = Alterar um loop de sua sequência normal.

# break =           usado para finalizar o loop inteiro.
# continue =        pular para a proxima interação do loop.
# pass =            não faz nada, apenas um tampa buraco.

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):

        if i == 13:
            pass
        else:
            print(i)
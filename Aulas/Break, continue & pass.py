# Loop Control Statements = modifica a execução de um loop a partir da sua sequência normal.

# break =       usado para finalizar completamente um loop
# continue =    pula para a proxíma interação do loop
# pass =        não faz nada, serve como um tampa buraco

while True:
    name = input("Enter your name: ")
    if name != "":                    # A junção do != e "" significa se ele não escrever nada.
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

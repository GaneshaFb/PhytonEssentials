# Tuple = Uma coleção que é ordenada e imutável
#         usada para agrupar dados relacionados.

student = ("Fabio",15,"male")

print(student.count("Fabio")) # Conta quantas vezes o item entre () aparece na tuple.
print(student.index("male")) # Mostra qual a posição númerica do item entre () na tuple.

for x in student:
    print(x)

if "Fabio" in student:
    print("Fabio is here!")

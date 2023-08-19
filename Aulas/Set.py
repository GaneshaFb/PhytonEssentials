# Set = Coleção que é desordenada, não indexada e sem valores duplicados.

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin") # Adiciona o item dentro dos () na set.
#utensils.remove("fork") # Remove o item dentro dos () da set.
#utensils.clear() # Remove todos os itens da set.
utensils.update(dishes) # Adiciona todos os elemetos do set entre () no set fora dos ().
dinner_table = utensils.union(dishes) # Cria um novo set unindo o set dentro dos () e o fora dos().

print(utensils.difference(dishes)) # Imprime os itens que o set de fora tem que o set de dentro dos () não tem.
print(utensils.intersection(dishes)) # Imprime os itens que o set de fora e o set de dentro dos () tem em comum.

for x in utensils:
    print(x)

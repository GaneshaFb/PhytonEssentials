# Dictionary = Uma mutavel, coleção não organizada de uma unica chave:valores pares
#              Rapida por causa que usa hashing, nos permitindo acesso ao valor rapidamente

capitals = {"Brasil":"Brasilia",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})           # Adiciona uma key e um valor par no dictionary.
capitals.update({"Brasil":"Rio Grande do Sul"}) # Atualiza uma key já existente no dictionary.
capitals.pop("China")                           # Retira a key dentro dos parenteses do dictionary.
capitals.clear()                                # Retira todas as keys do dictionary.

#print(capitals["Brasil"])              # Imprime o valor par da key entre colchetes.
#print(capitals.get("USA"))             # Checa se a key entre parenteses existe no dictionary.
#print(capitals.keys())                 # Imprime só as keys do dictionary.
#print(capitals.values())               # Imprime só os valores pares do dictionary.
#print(capitals.items())                # Imprime o dictionary inteiro.

# Para imprimir o dicionário com as keys e valores pares um em baixo do outro use o loop:

for key,value in capitals.items():
    print(key, value)

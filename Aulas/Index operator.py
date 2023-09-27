# Index operator [] = Da acesso para uma sequência de elementos (str,list,tuples)

name = "fabio Junior"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[:5].upper()   # Indica o "range" da str que você quer pegar e deixa tudo Maisculo.
last_name = name[6:].lower()    # Indica o "range" da str que você quer pegar e deixa tudo Minusculo.
last_carachter = name[-1]       # Pega o ultímo caractere da str.

print(name)
print(first_name)
print(last_name)
print(last_carachter)

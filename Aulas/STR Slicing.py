# Slicing str = cria uma substring extraindo os elementos de outra string.
#               indexing[] or slice()
#               [inicio:fim:intervalo]

name = "Fabio Junior"

first_name = name[:5]           # [inicio:3]
last_name = name[6:]            # [4:fim]
funky_name = name[::3]          # [inicio:fim:2]
reversed_name = name[::-1]      # [inicio:fim:-1]

print("---=( Indexing )=---")
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

# Se você imaginar que no final do link tem um 0 os números antes são negativos e você usa essa lógica para definir o fim.

slice = slice(7,-4)

print("---=( Slicing )=---")
print(website1[slice])
print(website2[slice])

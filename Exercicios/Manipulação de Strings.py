palavra = str(input("Qual palavra? "))

p_invertida = palavra[::-1]

print("O total de letras nessa palavra é ",len(palavra))
print("Essa palavra invertida é ",p_invertida)
print("Essa palavra em maiscúlo fica assim ",palavra.upper())
print("Essa palavra em minúsculo fica assim ",palavra.lower())

if palavra == p_invertida:
    print("Essa palavra é um palíndromo!")
else:
    print("Essa palavra não é um palíndromo!")
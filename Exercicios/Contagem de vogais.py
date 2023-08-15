palavra = input("Qual a palavra? ").lower()

vogais = "aeiou"
contador = 0

for vogal in vogais:
    contador += palavra.count(vogal)

print("Essa palavra tem", contador, "vogais!")

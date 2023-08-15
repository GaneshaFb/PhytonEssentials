frase = str(input("Qual frase? "))

comprimento = len(frase)
divisor = comprimento // 2 # Usar divisão inteira para garantir que o índice seja um número inteiro

print("Comprimento da frase:", comprimento)
print("Frase em letras maiúsculas:", frase.upper())
print("Frase em letras minúsculas:", frase.lower())
print("Primeira metade da frase:", frase[:divisor])
print("Segunda metade da frase:", frase[divisor:])

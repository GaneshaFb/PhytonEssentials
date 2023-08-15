num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Trocar os valores usando Multiple assignment
num1, num2 = num2, num1

print("Após a troca, o primeiro número é:", num1)
print("Após a troca, o segundo número é:", num2)
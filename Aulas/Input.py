# Input = você faz uma pergunta ao usuário e armazena a resposta em uma variável

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age + 1

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+" cm tall")

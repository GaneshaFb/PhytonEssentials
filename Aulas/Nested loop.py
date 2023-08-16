# Nested loops = A "inner loop" concluirá todas as suas iterações antes
#                de concluir uma iteração da "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # O [end=""] impede do print pular para a próxima linha. Isso significa que os símbolos serão impressos lado a lado na mesma linha.
    print()

# Keyword arguments = Argumentos que são precedidos por um indentificador quando nos passamos eles por uma função.
#                     A ordem desses argumentos não importa, diferente de "positional arguments".
#                     Python conhece os nomes dos argumentos que nossa função recebe.

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)


hello(first="Fabio",middle="Augusto",last="Junior")

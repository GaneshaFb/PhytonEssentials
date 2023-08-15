import time
# For loop = uma declaração que executará seu bloco de código
#            um número limitado de vezes
#
#            while loop = ilimitado
#            for loop = limitado

for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "Fabio Junior":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")

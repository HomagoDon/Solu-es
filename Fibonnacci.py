
n = int(input("digite o tamanho da seguência: "))
a = 0
b = 1
c = 0
while c <= n:
    print(f'{c}')
    c = a + b
    a = b
    b = c
print('Terminado')
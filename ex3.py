x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
cont = 0
while x > 0:
    x -= y
    cont += 1
    if x < 0:
        cont -= 1
print(cont)
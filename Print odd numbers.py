number = int(input("Introduce an positive integer number\n"))
string = ""
for i in range(1, number + 1):
    if i % 2 != 0:
        string += str(i) #La función str convierte su argumento en str
        string += ", " #El operador + concatena cadenas de carácteres
print(string)
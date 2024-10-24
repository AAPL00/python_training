number1 = int(input("Introduce the first number\n"))  #La función input() captura lo que se introduce como string y debe ser
number2 = int(input("Introduce the second \n"))       #convertido en este caso con la función int()
cocient = number1 // number2
rest = number1 % number2
print(f"The division between {number1} and {number2} is equal to {cocient} with rest {rest}")
#Con este formato particular imprimir es muy fácil cuando debes introducir variables en el texto
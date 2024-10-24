phrase = input("Introduce some clever phrase\n")  #El parámetro prompt no introduce salto de línea automáticamente
reversed_phrase = ""
#A la función range le puedes especificar un tercer argumento significando el paso por ejemplo (0, 5, 2) 
#en cada iteracion i+=2
#En la función range el primer parámetro es inclusivo mientras que el segundo parámetro es exclusivo
for i in range(1, len(phrase) + 1):  #La función len devuelve el tamaño de la colección
    reversed_phrase += phrase[-i]
print(reversed_phrase)

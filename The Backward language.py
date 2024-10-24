print("Introduce some clever phrase")
phrase = input()
reversed_phrase = ""

#a la funcion range le puedes especificar un tercer parametro significando el paso por ejemplo (0, 5, 2) 
#en cada iteracion i+=2

#la funcion len devuelve el tama;o de la coleccion

#en la funcion range el primer parametro es inclusivo mientras que el segundo parametro es exclusivo

for i in range(1, len(phrase) + 1):
    reversed_phrase += phrase[-i]
print(reversed_phrase)

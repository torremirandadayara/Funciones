def cantidad_de_letras_a(palabras):
    letras_a = 0
    for x in range(len(palabras)):
        if palabras[x] == "a" or palabras[x] == "A":
            letras_a = letras_a + 1
    return letras_a


# bloque prinicpal
palabra = input("Ingrese una palabra: ")
print("-----------------------------------------------------")
print("La palabra", palabra, "tiene", cantidad_de_letras_a(palabra), "a.")

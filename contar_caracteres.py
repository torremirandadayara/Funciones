def largo(cadena):
    return len(cadena)


# bloque principal del programa
nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")
la1 = largo(nombre1)
la2 = largo(nombre2)
if la1 == la2:
    print("Los nombres: ", nombre1, "y", nombre2, "tienen la misma cantidad de caracteres.")
else:
    if la1 > la2:
        print(nombre1, "es mas largo.")
    else:
        print(nombre2, "es mas largo.")

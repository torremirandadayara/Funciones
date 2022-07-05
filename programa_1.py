def retornar_perimetro(a):
    a = (a * 4)
    return a


# bloque principal del programa
lado = int(input("Ingrese el valor del lado del cuadrado: "))
print("------------------------------------")
perimetro = retornar_perimetro(lado)
print("El perimetro del cuadrado es: ", perimetro)

def retornar_superficie(b, h):
    a = (b * h)
    return a


print("PRIMER RECTANGULO")
base1 = int(input("Ingrese el valor de la base: "))
altura1 = int(input("Ingrese el valor de la altura: "))
print("La superficie del primer rectanculo es: ", retornar_superficie(base1, altura1))
print("-----------------------------------------------")
print("SEGUNDO RECTANGULO")
base2 = int(input("Ingrese el valor de la base: "))
altura2 = int(input("Ingrese el valor de la altura: "))
print("La superficie del segundo rectanculo es: ", retornar_superficie(base2, altura2))
print("=====================================================")
if retornar_superficie(base1, altura1) > retornar_superficie(base2, altura2):
    print("La superficie del primer rectangulo es mayor.")
else:
    print("La superficie del segundo rectangulo es mayor.")

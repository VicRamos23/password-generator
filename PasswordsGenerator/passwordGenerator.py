import random
import string


def UserConfig():
    while True:
        longi = int(input("Ingrese la longitud de la contraseña entre 8 y 14: "))
        if longi < 8:
            print("El mínimo de caracteres es 8!")
        elif longi > 14:
            print("El máximo de caracteres es 14!")
        else:
            break

    mayus = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    minus = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
    num = input("¿Incluir números? (s/n): ").lower() == 's'
    car_esp = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    # Cantidad de contraseñas a generar
    while True:
        try:
            cantidad = int(input("¿Cuántas contraseñas deseas generar?: "))
            if cantidad <=0:
                print("La cantidad debe ser un valor entero positivo")
            else:
                break
        except ValueError:
                print("Ingrese un número entero")

    return longi, mayus, minus, num, car_esp, cantidad


def PasswordGen(longi, mayus, minus, num, car_esp):
    caracteres = ""
    if mayus:
        caracteres += string.ascii_uppercase
    if minus:
        caracteres += string.ascii_lowercase
    if num:
        caracteres += string.digits
    if car_esp:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de caracter.")

    password = ''.join(random.choice(caracteres) for x in range(longi))
    return password


def main():
    longi, mayus, minus, num, car_esp, cantidad = UserConfig()

    for i in range(cantidad):
        contrasena = PasswordGen(longi, mayus, minus, num, car_esp)
        print("Contraseña generada: ", contrasena)

    input("Presiona Enter para salir...")


if __name__ == "__main__":
    main()


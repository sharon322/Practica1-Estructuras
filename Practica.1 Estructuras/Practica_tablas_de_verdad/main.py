from tablas_verdad import TablaVerdad
from entrada import obtener_entrada

def main():
    while True:
        print("\n**Menu de opciones**")
        print("1. Generar tabla de verdad")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            try:
                variables = obtener_entrada("Ingrese las variables que desea utilizar, separadas por comas (maximo 3): ", 3)
                expresiones = obtener_entrada("Ingrese las expresiones logicas: ", 3)
                tabla = TablaVerdad(variables, expresiones)
                tabla.generar_tabla()
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            print("Programa finalizado…")
            break
        else:
            print("Seleccion no valida. Por favor, intentelo nuevamente.")

if __name__ == "__main__":
    main()
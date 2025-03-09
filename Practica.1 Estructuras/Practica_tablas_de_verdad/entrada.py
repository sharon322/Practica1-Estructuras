def obtener_entrada(mensaje, max_elementos):
    # Solicita la entrada del usuario y asegura que esté en el formato correcto
    while True:
        # Solicita la entrada del usuario, elimina espacios en blanco y divide por comas
        entrada = input(mensaje).replace(" ", "").split(',')

        # Verifica que la cantidad de elementos esté dentro del rango permitido
        if 1 <= len(entrada) <= max_elementos:
            # Verifica que todos los elementos sean letras
            if all(e.isalpha() for e in entrada):
                return list(entrada)  # Devuelve la lista de elementos, manteniendo el orden
            else:
                print("Error: Solo se pueden ingresar letras.")
        else:
            # Mensaje de error si la cantidad de elementos no es válida
            print(f"Error: Debe ingresar entre 1 y {max_elementos} elementos separados por comas.")


# replace(' ', ''): Sustituye todos los espacios en blanco en la entrada del usuario por una cadena vacía, eliminándolos.
# split(','): Divide la cadena resultante en una lista de elementos utilizando la coma como delimitador.
#e.isalpha(): método de cadena Python que devuelve True si todos los caracteres son letras. Si está vacío o contiene letras devuelve False.

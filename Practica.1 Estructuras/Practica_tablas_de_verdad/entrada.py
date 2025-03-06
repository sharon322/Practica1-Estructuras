def obtener_entrada(mensaje, max_elementos):
    while True:
        entrada = input(mensaje).replace(" ", "").split(',')
        if 1 <= len(entrada) <= max_elementos:
            # Verifica que todos los elementos sean letras
            if all(e.isalpha() for e in entrada):
                return list(entrada)  # Devuelve la lista de elementos, manteniendo el orden
            else:
                print("Error: Todos los elementos deben ser letras.")
        else:
            print(f"Error: Debe ingresar entre 1 y {max_elementos} elementos separados por comas.")

#replace= (' ')sustituye todos los espacios en blanco en la entrada del usuario por una cadena vacía, efectivamente eliminándolos.
#split(',') divide la cadena resultante en una lista de elementos utilizando la coma como delimitador.
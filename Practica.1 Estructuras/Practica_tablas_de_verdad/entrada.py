def obtener_entrada(mensaje, max_elementos):
    while True:                                                 
        entrada = input(mensaje).replace(" ", "").split(',')    # Solicita la entrada del usuario y elimina espacios en blanco
        if 1 <= len(entrada) <= max_elementos:
            return list(entrada)  # Convertir a lista en lugar de set para mantener el orden
        print(f"Error: Debe ingresar entre 1 y {max_elementos} elementos separados por comas.")

#replace= (' ')sustituye todos los espacios en blanco en la entrada del usuario por una cadena vacía, efectivamente eliminándolos.
#split(',') divide la cadena resultante en una lista de elementos utilizando la coma como delimitador.
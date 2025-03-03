def obtener_entrada(mensaje, max_elementos):
    while True:
        entrada = input(mensaje).replace(" ", "").split(',')
        if 1 <= len(entrada) <= max_elementos:
            return list(entrada)  # Convertir a lista en lugar de set para mantener el orden
        print(f"Error: Debe ingresar entre 1 y {max_elementos} elementos separados por comas.")
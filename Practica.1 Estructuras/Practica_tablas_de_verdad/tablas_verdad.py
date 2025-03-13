class TablaVerdad:
    operadores = {
        'AND': lambda p, q: p and q,  # Operador lógico AND
        'OR': lambda p, q: p or q,      # Operador lógico OR
        'XOR': lambda p, q: p != q,     # Operador lógico XOR
        'IMPLIES': lambda p, q: (not p) or q, #alt+26
        'DIMPLIES': lambda p, q: p == q  #alt+27 y 26
        }
    
    def __init__(self, variables, expresiones): #Inicializa la clase con variables y expresiones lógicas
        self.variables = list(variables)
        self.expresiones = expresiones
        self.validar_expresiones()

    def validar_expresiones(self):      #Valida que las expresiones solo contengan las variables definidas
        for expr in self.expresiones:
            # Extraer variables válidas de la expresión
            vars_en_expr = set(filter(lambda x: x in self.variables, expr.split()))
            if not vars_en_expr.issubset(set(self.variables)):    #Conjuntos,subconjuntos
                raise ValueError(f"Las variables {vars_en_expr - set(self.variables)} no fueron ingresadas previamente.")

    def evaluar_expresion(self, expr, valores):        #Evalúa una expresión lógica dada un conjunto de valores para las variables
        if expr in self.variables:
            return valores[self.variables.index(expr)]      # Devuelve el valor de la variable

        for op in sorted(self.operadores.keys(), key=len, reverse=True):    # Busca y evalúa el operador en la expresión
            if op in expr:
                partes = expr.split(op)
                if len(partes) == 2:
                    p, q = partes
                    return self.operadores[op](
                        self.evaluar_expresion(p.strip(), valores),
                        self.evaluar_expresion(q.strip(), valores)
                    )
                else:
                    raise ValueError(f"Expresion no valida: {expr}")

        raise ValueError(f"Expresion no valida: {expr}")

    def generar_combinaciones(self, n):     #Genera todas las combinaciones posibles de valores booleanos para n variables
        return [[(i >> j) & 1 for j in range(n - 1, -1, -1)] for i in range(2 ** n)]

    def generar_tabla(self):      #Genera e imprime la tabla de verdad para las expresiones lógicas 
        print("\n---- A continuacion se presenta la tabla de verdad generada ----")
        encabezado = " | ".join(self.variables) + " | " + " | ".join(self.expresiones)
        print(encabezado)
        print("-" * len(encabezado))

        # Generar combinaciones de valores
        combinaciones = self.generar_combinaciones(len(self.variables))

    # Evaluar cada expresión y almacenar los resultados
        for valores in combinaciones:
            try:
                resultados = [int(self.evaluar_expresion(expr, valores)) for expr in self.expresiones]
                fila = " | ".join(map(str, valores)) + " | " + " | ".join(map(str, resultados))
                print(fila)
            except ValueError as e:
                print(f"Error en la evaluacion de la tabla: {e}")

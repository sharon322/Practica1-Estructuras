class TablaVerdad:
    operadores = {
        'AND': lambda p, q: p and q,
        'OR': lambda p, q: p or q,
        'XOR': lambda p, q: p != q,
        '→': lambda p, q: (not p) or q, #alt+26
        '←→': lambda p, q: p == q  #alt+27 y 26
        }
    
    def __init__(self, variables, expresiones):
        self.variables = list(variables)
        self.expresiones = expresiones
        self.validar_expresiones()

    def validar_expresiones(self):
        for expr in self.expresiones:
            # Extraer variables válidas de la expresión
            vars_en_expr = set(filter(lambda x: x in self.variables, expr.split()))
            if not vars_en_expr.issubset(set(self.variables)):
                raise ValueError(f"Las variables {vars_en_expr - set(self.variables)} no fueron ingresadas previamente.")

    def evaluar_expresion(self, expr, valores):
        if expr in self.variables:
            return valores[self.variables.index(expr)]

        for op in sorted(self.operadores.keys(), key=len, reverse=True): 
            if op in expr:
                partes = expr.split(op)
                if len(partes) == 2:
                    p, q = partes
                    return self.operadores[op](
                        self.evaluar_expresion(p.strip(), valores),
                        self.evaluar_expresion(q.strip(), valores)
                    )
                else:
                    raise ValueError(f"Expresión no válida: {expr}")

        raise ValueError(f"Expresión no válida: {expr}")

    def generar_combinaciones(self, n):
        return [[(i >> j) & 1 for j in range(n - 1, -1, -1)] for i in range(2 ** n)]

    def generar_tabla(self):
        print("\n---- Se ha generado la siguiente tabla de verdad ----")
        encabezado = " | ".join(self.variables) + " | " + " | ".join(self.expresiones)
        print(encabezado)
        print("-" * len(encabezado))

        combinaciones = self.generar_combinaciones(len(self.variables))

        for valores in combinaciones:
            try:
                resultados = [int(self.evaluar_expresion(expr, valores)) for expr in self.expresiones]
                fila = " | ".join(map(str, valores)) + " | " + " | ".join(map(str, resultados))
                print(fila)
            except ValueError as e:
                print(f"Error en la evaluación de la tabla: {e}")

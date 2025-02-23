class TablaVerdad:
    operadores = {
        '^': lambda p, q: p and q,
        '|': lambda p, q: p or q,
        '⊕': lambda p, q: p != q,
        '→': lambda p, q: (not p) or q,
        '←→': lambda p, q: p == q
    }

print()
print()
# Este script calcula el interés compuesto anual dado el principal, la tasa de interés anual y el período de tiempo en años.
# No utilizar en producción. Solo para fines de muestra.

# Autor: Upkar Lidder (IBM)

# Entrada:
# p, monto principal
# t, período de tiempo en años
# r, tasa de interés anual

# Salida:
# interés compuesto = p * (1 + r/100)^t

def compound_interest(p, t, r):
    return p * (pow((1 + r / 100), t))

if __name__ == "__main__":
    p = float(input("Introduce el monto principal: "))
    t = float(input("Introduce el período de tiempo en años: "))
    r = float(input("Introduce la tasa de interés anual: "))

    print("El interés compuesto es {:.2f}".format(compound_interest(p, t, r)))

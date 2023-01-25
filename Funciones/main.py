# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


anio = 2023
print(f"El anio {anio} es bisiesto: {es_bisiesto(2023)}")

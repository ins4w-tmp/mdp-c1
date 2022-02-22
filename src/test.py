# 0. Enunciado
"""
Escribir un programa que recorra los números enteros del 1 al 1000 (incluído) y acumule la suma parcial de números pares y de números impares (por separado) para calcular finalmente el valor absoluto de la diferencia de las dos sumas acumuladas.

Ejemplo de la salida:
acum_par: 249500
acum_impar: 250000
diff: 500

"""

# 1. Examples (Corner Cases)
# () => ()

# 2. Coding
def someFunction():

    suma_impares = 0
    suma_pares = 0

    for num in range(1, 1001):
        if num % 2 == 0:
            suma_pares += num
        if num % 2 == 1:
            suma_impares += num

    return abs(suma_impares - suma_pares)


# 3. Examples Tests
print(someFunction())
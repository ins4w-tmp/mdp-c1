"""
Escribir un programa que genere secuencias aleatorias de bases nitrogenadas de ADN de una longitud de 200 bases, mostrando 60 bases por línea. Cada base está representada  por una de las siguientes letras: a (adenina), c (citosina), g (guanina) y t (timina). Considere adicionalmente que la misma base podrá aparecer solo 2 veces seguidas como máximo la primera vez, luego 3 veces seguidas como máximo y finalmente 4 veces seguidas como máximo, luego de lo cuál el nuevo máximo regresa a ser 2 veces, de manera cíclica.

Ejemplo de la salida:
tcggacgccttaagataaatggttgctcaggcgtactgggaaggggatctcggtttagaa
ctctatgtttggtcgagggacttctggtagatatggtgacgtgtgttgcgactgtgtgag
gataacactagcgaaatcagagtaccgcaatccaaggactacctgtacggcagttagatg
agcatgtcgcccacccc

"""

from random import randint

# 1. Examples (Corner Cases)
# () => ()

# 2. Coding
def someFunction():
    bases = {'a': 0, 'c': 0, 'g': 0, 't': 0}
    bases_keys = list(bases.keys()) # ['a', 'c', 'g', 't']

    for i in range(1, 201):

        # obtener base de bases_keys
        base = bases_keys[randint(0,len(bases) - 1)]

        # si la base obtenida no esta en el diccionario de bases se quita la base de bases_keys y se genera una nueva base
        if base not in bases:
            bases_keys.pop(base)
            base = bases_keys[randint(0,len(bases) - 1)]

        # se aumenta la base al contador de bases en el diccionario
        bases[base] += 1

        # si la base o nueva base se ha repetido 2, 3, o 4 veces se reinicia el contador de la base a 0, pero cuando se llega a 4 se quita la base del diccionario
        if bases[base] == 2 or bases[base] == 3 or bases[base] == 4:
            bases[base] = 0
            if bases[base] == 4:
                del bases[base]

        
        if i % 60 == 0:
            print(base)
        else:
            print(base, end="")

# 3. Examples Tests
print(someFunction())
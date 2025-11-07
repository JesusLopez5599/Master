#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ===================================================================
# Introducción a la Programación con Python y los Paradigmas de Datos
# Primera entrega (2025-26)
# ===================================================================

# **************************************************************
# APELLIDOS: López Guerrero
# NOMBRE: Jesús
# **************************************************************


# Escribir el código Python de las funciones que se piden en el
# espacio que se deja a continuación de cada ejercicio.

# IMPORTANTE: NO CAMBIAR EL NOMBRE A LAS FUNCIONES QUE SE PIDEN  (aquellas funciones 
# con un nombre distinto al que se pide en el ejercicio NO se corregirán).




# -----------
# EJERCICIO 1
# -----------

# Definir, usando while, una función que comprueba si una lista numérica está ordenada de menor a mayor. 

# Ejemplos:

# >>> ordenada([2,4,5,5,7,9,11])
# True
# >>> ordenada([2,4,5,5,2,7,5,8,8])
# False

import numbers

def ordenada (l):
    if all(isinstance(x, numbers.Number) for x in l) == False: #compruebo si es una lista numérica
           return ("No es una lista entera numérica")
    else:
        i=0
        while i<len(l) -1:
            if l[i]>l[i+1]:
                return False
            else:
                i += 1
        return True
            





# -----------
# EJERCICIO 2
# -----------

# Definir una función traspuesta_destr(a), que recibiendo una matriz cuadrada
# a (en forma de lista de listas) cambia esa matriz de entrada para que
# su contenido una vez sea ejecutada la llamada traspuesta_destr(a)
# sea la traspuesta de la original. 


# Ejemplos:

# >>> a=[[5,6,-1,3],[2,5,1,8],[3,14,-4,8],[9,1,4,5]]
# >>> traspuesta_destr(a)
# >>> a
# [[5,2,3,9],[6,5,14,1],[-1,1,-4,4],[3,8,8,5]]

def cuadrada(a): #para comprobar que es una matriz cuadrada
    if not a: #Suponemos que la matriz es no vacía
        return False
    filas= len(a)
    for fila in a:
        if len(fila) != filas:
            return False
    return True
    
def traspuesta_destr(a):
    l=len(a)
    if cuadrada(a)== False:
        return ("La matriz no es cuadrada")
    else:
        for i in range (l):
            for j in range (i+1, l):
                a [i][j], a[j][i] = a [j][i], a [i][j]
    print(a)





# -----------
# EJERCICIO 3
# -----------


# (a) Definir una función diferencias(l) tal que dada una lista no vacía
# de números [x1,x2,...,xn]  calcula la lista de diferencias
# [x2-x1,x3-x2,...,xn-x(n-1)]. Hacerlo usando un bucle range. 

# Ejemplo:

# >>> diferencias([5,2,4,8,9,9,2,3])
# [-3,2,4,1,0,-7,1]


def numeros_novacio(l):
    return bool(l) and all(isinstance(x, numbers.Number) for x in l)

def diferencias (l):
    resultado=[]
    if numeros_novacio(l)== False:
        return ("La lista no cumple las condiciones necesarias")
    else:
        for i in range(1,len(l)):
            resultado.append(l[i]-l[i-1])
    return resultado
            

# (b) Hacer una versión de la función anterior, diferencias_2, usando
# lista por comprensión, y sin usar range (Consejo: usar zip).  
def diferencias_2 (l):
    if not numeros_novacio(l):
        return "La lista no cumple las condiciones necesarias"
    return [x - y for x, y in zip(l[1:], l)]




# -----------
# EJERCICIO 4
# -----------

# Una matriz cuadrada de tamaño nxn es un cuadrado mágico si sus
# elementos son números distintos entre 1 y n*n y tanto sus filas,
# como sus columnas, como sus dos diagonales principales, suman la
# misma cantidad.

# Definir una función es_cuadrado_mágico(a) que recibiendo una matriz
# cuadrada a (representada mediante listas de listas), devuelve un
# booleano indicando si es o no un cuadrado mágico.

# Supondremos (sin necesidad de comprobarlo) que todos los elementos
# de a son números naturales positivos menores o iguales que n*n. 
# Consejo: usar la función sum que suma los elementos de una lista. 

def todo_distinto(a):
    l=len(a)
    for i in range(l):
        for j in range(l):
            for k in range (l):
                for n in range(l):
                    if i==k and j ==n:
                        continue
                    if a[i][j] == a[k][n]:
                        return False
    return True
            
def es_cuadrado_mágico(a):
    l=len(a)
    suma=sum(a[0])
    if not cuadrada(a):
        return False
    
    if todo_distinto(a) == False:
        return (" Hay elementos repetidos en la matriz")
    
    else:
        for i in range(1,l):
            if sum(a[i]) != suma:
                return False
        for j in range(l):
            if sum(a[i][j] for i in range(l)) != suma:
                return False

    # Comprobar diagonales
    diag1 = sum(a[i][i] for i in range(l))
    diag2 = sum(a[i][l-1-i] for i in range(l))
    if diag1 != suma or diag2 != suma:
        return False

    return True
            
    





# -----------
# EJERCICIO 5
# -----------

# Definir una función `todos_distintos(l)` que recibiendo una lista `l`, comprueba
# si `l`tiene todos sus elementos distintos entre sí. NO usar el tipo de dato "set" de Python.


# Ejemplo:

# >>> todos_distintos([3,7,8,11,13])
# True

# >>> todos_distintos([3,5,1,6,5,8,9,0,3])
# False

def todos_distintos(l):
    n=len(l)
    for i in range(n):
        for k in range(n):
            if i == k:
                    continue
            else:
                if l[i] == l[k]:
                    return False
    return True
                
                    






# -----------
# EJERCICIO 6
# -----------


# Definir una función que `todos_distintos_mat(a)` que recibiendo una matriz `a` 
# (representada como lista de listas) comprueba si `a` tiene todos sus elementos 
# distintos entre sí. Hacerlo sin "aplanar" la matriz y sin usar la función del
# apartado anterior

 
# Ejemplos:

a1=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

a2=[[1,2,3,4],
    [4,6,7,8],
    [9,10,3,12],
    [13,2,14,15]]

a3=[[1,2,3,4],
    [4,6,7,8],
    [9,10,9,12]]

# >>> todos_distintos_mat(a1)
# True

# >>> todos_distintos_mat(a2)
# False      

# >>> todos_distintos_mat(a3)
# False      

#Lo definí en un ejercicio anterior
def todos_distintos_mat(a):
    l=len(a)
    for i in range(l):
        for j in range(l):
            for k in range (l):
                for n in range(l):
                    if i==k and j ==n:
                        continue
                    if a[i][j] == a[k][n]:
                        return False
    return True
# ------------
# EJERCICIO 7
# ------------
#

# Usando definiciones por comprensión, definir una función
# 'matriz_identidad(n)' que devuelva (en forma de lista de listas) la
# matriz identidad de tamaño n.

# Ejemplos:

# >>> matriz_identidad(3)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# >>> matriz_identidad(9)

#[[1, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 1, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 1, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 1, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 1]]

def matriz_identidad(n):
    return [[1 if i== j else 0 for j in range (n)] for i in range(n)]
        


# ------------
# EJERCICIO 8
# ------------
#

# La función all (predifinida) de python recibe como entrada una
# secuencia o iterable y devuelve verdadero si todos sus elelemntos
# son verdaderos, falso en caso contrario.

# Por ejemplo:

# Todos los nombres de la lista empiezan por "A"
# >>> all((x[0]=="A" for x in ["Alberto","Antonio","Alfonso", "Adán"]))
# True

# No todos empiezan por "A"
# >>> all((x[0]=="A" for x in ["Alberto","Juan","Alfonso", "Luis"]))
# False

# Todas las potencias de 3 hasta la 100 son impares:
# >>> all(((3**x)%2==1 for x in range(1,100))) 
# True

# La función any (predefinida de python) es dual a all. Devuelve
# verdadero si algno de los elelemntos de la secuencia es verdadero,
# falso en caso contrario.

# Se pide definir, usando all y definición por comprensión, una
# función 'es_primo(n)' que comprueba si un núero natural n es primo.

def es_primo(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, n))



# ------------
# EJERCICIO 8
# ------------
#

# Es el ejercicio 19 de la primera relación de ejercicios


# Definir una función factoriza_primos(n), que recibiendo como entrada un número 
# natural n, cuya factorizaciçón en números primos es n=p1^e1*p2^e2*...*p_m^em,
# devueve la lista [(p1,e1),(p2,e2),...,(p_m,em)] 

# Ejemplos:

# >>> factoriza_primos(171)
# >>> [(3, 2), (19, 1)]
# >>> factoriza_primos(272250)
# [(2, 1), (3, 2), (5, 3), (11, 2)]
# >>> factoriza_primos(358695540883235472)
# [(2, 4), (3, 1), (7, 1), (83, 2), (173, 5)]

# NOTA: Hacerlo sin usar una lista predefinida de números primos, 
# y sin usar la función que se pide en el ejercicio anterior. 

# SUGERENCIA: se puede hacer mediante dos bucles "while" anidados. 
# El más interno calcula el exponente de cada posible divisor del número, 
# dividiendo con ese divisor mientras sea divisible. 
# El bucle externo contendría al bucle interno y además iría incrementando en
# uno (o en dos, si sólo se considera los impares) el valor de ese posible
# divisor.     
# Para dividir, usar el operador // de división entera. 


def factoriza_primos(n):
    if n<2:
        return []
    factores= []
    
    # haremos por separado el 2
    e=0
    while n % 2 ==0:
        n //=2
        e +=1
    if e>0:
        return factores.append((2,e))
    
    #impares
    d=3
    while d*d <=n:
        e=0
        while n%d ==0:
            n//= d
            e +=1
        if e > 0 :
            factores.append((d,e))
        d +=2
    if n > 1:
        factores.append((n, 1))

    return factores
            
    





# -----------
# EJERCICIO 9
# -----------

# El siguiente diccionario muestra la codificación en Morse de las letras y 
# y de algunos símbolos: 

CÓDIGOS_MORSE =   { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Definir funciones codifica_morse(m) y decodifica_morse(m) que recibiendo un 
# string m con un mensaje (en castellano o en morse, respectivamente), devuelve 
# el correspondiente mensaje codificado o decodificado, respectivamente. 

# En la codificación morse, se entiende que los códigos de cada letra o símbolo
# se separan por un espacio en blanco. Por simplificar, supondremos también
# que en una frase en castellano las palabras se separan por un guión, 
# y que se escribe en mayúscula sin tildes.


# Ejemplos:

# >>> codifica_morse("ESTOY-EN-CLASE")
# '. ... - --- -.-- -....- . -. -....- -.-. .-.. .- ... .'
# >>> decodifica_morse('. ... - --- -.-- -....- . -. -....- -.-. .-.. .- ... .')
# 'ESTOY-EN-CLASE'

def codifica_morse(l):
    resultado=" "
    for caracter in l.upper():
        if caracter in CÓDIGOS_MORSE:
            resultado += CÓDIGOS_MORSE[caracter] + " "
        else:
            resultado += caracter
    return resultado
    
def decodifica_morse(l):
    #invertimos el diccionario
    morse_a_letra= {valor:clave for clave,valor in CÓDIGOS_MORSE.items()}
    
    resultado=""
    letras= l.split()
    
    for codigo in letras:
        if codigo in morse_a_letra:
            resultado += morse_a_letra[codigo]
        else:
            resultado += ""
        
    return resultado
    
        






# ------------
# EJERCICIO 10
# ------------
#
# 
# Supongamos que tenemos almacenada, usando diccionario, la información sobre
# el grupo de los alumnos de un curso. Para ello, usamos como clave el nombre
# de los alumnos de un grupo y como valor el grupo que tienen asignado. 

# 1) Definir una función alumnos_grupo(d) que a partir de un diccionario
# de ese tipo, devuelve otro diccionario cuyas claves son los nombres de los
# grupos y cuyo valor asignado a cada clave es la lista los alumnos que
# forman parte del grupo.

# Ejemplos:

# >>> alum={"Juan":"G1", "Rosa":"G2"  , "Joaquín":"G1"   ,"Carmen":"G2"  , 
#           "Isabel":"G1" , "Rocío":"G3" , "Bernardo":"G3", "Jesús":"G2"}
# >>> grupos=alumnos_grupo(alum)
# >>> grupos
# {'G3': ['Rocío', 'Bernardo'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Juan', 'Joaquín']}

def alumnos_grupo (d):
    grupos={}
    for niño, grupo in d.items():
        #si el grupo no está en el diccionario, lo creamos como lista vacía
        if grupo not in grupos:
            grupos[grupo] = []
        #Agregamos el alumno a la lista correspondiente
        grupos[grupo].append(niño)
        
    for g in grupos:
            grupos[g].sort(reverse=True)
        
    grupos_ordenados = dict(sorted(grupos.items(), reverse=True))

    return grupos_ordenados


# 2) Definir una función nuevo_alumno(dict_n,dict_g,nombre,grupo) tal que
# supuesto que dict_n y dict_g son dos variables conteniendo respectivamente
# el grupo de cada alumno y los alumnos de cada grupo, introduce un nuevo
# alumno con su nombre y grupo, modificando adecuadamente tanto dict_n como
# dict_g. Si el alumno ya está en los diccionarios, modificar el dato
# existente (en ese caso, si además el grupo que se quiere asignar no coincide
# que el que ya tiene se mostrará un mensaje de advertencia). Si se asigna un
# grupo que no está dado de alta, la correspondiente entrada se debe añadir al
# diccionario de grupos.

# Ejemplos:

# >>> nuevo_alumno(alum,grupos,"Bernardo","G3")
# Nog actualizado. El alumno Bernardo ya está dado de alta en el grupo G3
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G3'}
# >>> nuevo_alumno(alum,grupos,"Bernardo","G1")
# El alumno Bernardo ya está dado de alta. Se cambia al grupo G1
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G3': ['Rocío'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Juan', 'Joaquín', 'Bernardo']}
# >>> nuevo_alumno(alum,grupos,"Ana","G3")
# Nuevo alumno Ana. Incluido en el grupo G3
# >>> nuevo_alumno(alum,grupos,"Juan","G4")
# El alumno Juan ya está dado de alta. Se cambia al grupo G4
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Ana': 'G3', 'Juan': 'G4', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G4': ['Juan'], 'G3': ['Rocío', 'Ana'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Joaquín', 'Bernardo']}
# --------------------------------------------------------------------------


def nuevo_alumno(dict_n,dict_g,nombre,grupo):
    
    #aseguramos que el grupo exista
    def asegurar_grupo(g):
        if g not in dict_g:
            dict_g[g] = []
    
    if nombre in dict_n:
        grupo_actual = dict_n[nombre]
        
        if grupo_actual == grupo:
            #Ya estaba en ese grupo
            asegurar_grupo(grupo)
            if nombre not in dict_g[grupo]:
                dict_g[grupo].append(nombre)
            print(f"No actualizado. El alumno {nombre} ya está dado de alta en el grupo {grupo}")
            return
            
        #Cambio de grupo
        #Quitar del grupo anterior
        if grupo_actual in dict_g and nombre in dict_g[grupo_actual]:
            dict_g[grupo_actual].remove(nombre)
        
        #Añadir al nuevo grupo
        asegurar_grupo(grupo)
        if nombre not in dict_g[grupo]:
           dict_g[grupo].append(nombre)

       # Actualizar mapping alumno->grupo
        dict_n[nombre] = grupo
        print(f"El alumno {nombre} ya está dado de alta. Se cambia al grupo {grupo}")
    else:
       # Nuevo alumno
       dict_n[nombre] = grupo
       asegurar_grupo(grupo)
       if nombre not in dict_g[grupo]:
           dict_g[grupo].append(nombre)
       print(f"Nuevo alumno {nombre}. Incluido en el grupo {grupo}")




# ------------
# EJERCICIO 11
# ------------

# Supongamos que tenemos una lista m cuyos elementos son (sub)listas y
# cada una de estas sublistas no tiene elementos repetidos. Usando
# definiciones por comprensión, definir una función 'interseccion(m)' que
# calcule su intersección: es decir, la lista de elementos que están
# en todas las sublistas.

# Por ejemplo:

# >>> interseccion([[1,2,3,4,5],[0,2,4,6,8],[2,4,8,10]])
# [2,4]
# >>> interseccion([["a","b","c","d"], ["b","f","g","d"],["x","d","b","y"]])
# ['b', 'd']

def interseccion(m):
    return [x for x in m[0] if all(x in sublista for sublista in m)]

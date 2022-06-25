# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:11:22 2021

@author: USUARIO
"""

"""

El siguiente código, desarrollado por el estudiante Víctor Manuel López Molina para la 
asignatura Programación, Linux y Bases de Datos del Máster en Bioinformática y Biología
Computacional de la UAM, consiste en una herramienta para manejar cadenas de DNA generadas
aleatoriamente. Esta herramienta, denominada DNA-Toolkit, permite crear cadenas aleatorias
de DNA, guardarlas en el directorio actual, cargar una secuencia de DNA, borrar un fichero, 
comprobar que una cadena de DNA es válida, insertar mutaciones puntuales en la misma, medir
las frecuencias de cada base nitrogenada y contar subsecuencias en la secuencia.

"""

import os
DNA='' #cadena en la que se guardará la cadena de DNA generada, hasta que se genere otra nueva o se produzcan cambios en la misma.
def DNA_toolkit(): #menú principal.
    opcion=0
    while opcion<=0 or opcion>7:
        try:
            print("----------------------------------------")
            print("DNA-Toolkit v0.1")
            print("Please, select an option: ")
            print("1 - Create new DNA chain") #creación de una cadena aleatoria de DNA.
            print("2 - Save DNA chain") #la nueva cadena se guarda en un fichero cuyo nombre puede definir el usuario.
            print("3 - Load DNA from disk") #cargar un archivo que contiene una cadena de DNA.
            print("4 - List all DNA info") #generar una lista con todos los archivos que contienen una cadena de DNA.
            print("5 - Delete DNA info") #borrar un archivo indicado por el usuario.
            print("6 - Operations with DNA") #se abre un submenú que permite manipular la cadena de DNA actual (o generar una nueva) y hacer operaciones con ella.
            print("7 - Exit") #la herramienta se cierra.
            if DNA=='': #inicialmente, la cadena DNA no tendrá ningún contenido.
                print('[[There is no DNA chain loaded]]')
            else:
                print('[[Current chain:',DNA,"]]") #si hay alguna cadena generada, la variable DNA pasa a ser la cadena de DNA actual (tras ser generada o tras haber mutado otra preexistente).
            print("----------------------------------------")
            opcion=eval(input("Please enter a number: ")) #el usuario introduce un número indicando la opción.
        except NameError: #si el usuario introduce una letra, aparece este mensaje.
            print("Oops! Please enter a number.")
        except SyntaxError: #si el usuario introduce un caracter especial, aparece este mensaje.
            print("Oops! Please enter a number.")
        else:
            print("You have selected option",opcion) #tras escoger una opción correctamente, se obtiene este mensaje.
    return opcion

#Función que genera una cadena de DNA aleatoria a partir de una cadena vacía.
from random import choice #choice devuelve un elemento aleatorio de una secuencia (en este caso, una tupla).
def DNA_chain(length):
    cadena='' #cadena vacía, en donde se guardará la cadena generada aleatoriamente.
    try:
        for x in range(length):
            cadena=cadena+choice('CGTA') #se genera una cadena de DNA aleatoria cuya longitud es elegida por el usuario.
    except TypeError: #si el usuario introduce un número decimal, aparece este mensaje. No se genera ninguna cadena, ni con un número decimal ni con uno entero negativo.
        print('Oops! Please enter an integer.')
    else:
        return cadena

#Función que permite guardar la cadena actual en un archivo con un nombre único.
import datetime
def save_chain(file):
    archivo=open(file,'w') #se abre el archivo cuyo nombre es definido por el usuario.
    print(DNA,file=archivo) #se guarda en dicho archivo la cadena de DNA actual.
    archivo.close() #se cierra el archivo.
    return file

#Función que permite cargar un fichero que contenga una cadena de DNA.
def load_DNA(file):
    archivo=open(file,'r') #se abre un archivo escogido por el usuario, el cual debe escoger este fichero a partir de una lista que se le muestra.
    lines=archivo.read() #se lee el fichero.
    archivo.close() #se cierra el fichero.
    return lines

#Función que permite generar una lista de los nombres de archivos que contienen cadenas de DNA.
def list_DNA():
    import os
    directory=os.getcwd() #directorio actual (que es el directorio donde se encuentra este fichero .py).
    files=os.listdir(directory) #lista de archivos presentes en dicho directorio.
    for f in files:
        if "_dna_string_" in f:
            print(f) #se muestra una lista de aquellos archivos que contengan en su título "_dna_string_", que identifica aquellos archivos que contienen cadenas de DNA.

#Función que, tras indicar el usuario el nombre de un archivo, borra este archivo.
def delete_DNA():
    import os
    print('\nList of files that can be deleted:')
    list_DNA() #se genera una lista de los archivos que se pueden borrar, es decir, aquellos que contengan en su título "_dna_string_".
    try:
        file=str(input('Please, from the above files, indicate the name of the file you want to delete: ')) #el usuario escoge el nombre del fichero que desea borrar.
        directory=os.getcwd() #directorio actual.
        path=os.path.join(directory,file) #ruta absoluta del archivo escogido.
        os.remove(path) #se elimina el archivo escogido.
    except FileNotFoundError: #Si el fichero indicado no existe, aparece este mensaje.
        print('Oops! Please enter a valid file name from the list above.')
    except IsADirectoryError: #Si el usuario indica un directorio, aparece este mensaje.
        print('Oops! Please enter a valid file name from the list above.')
    else:
        return file

exitCode=7
x=0
while x!=exitCode: #siempre y cuando la opción no sea 7 (salir), ocurre lo siguiente:
    x=DNA_toolkit()
    if(x!=exitCode):
        if(x==1): #opción 1
            try:
                length_option=eval(input('Please, provide the length of the DNA chain: ')) #el usuario escoge la longitud de la cadena de DNA aleatoria.
            except NameError: #si el usuario introduce una letra, aparece este mensaje de error.
                print("Oops! Please enter a number.") 
            except SyntaxError: #si el usuario introduce un carácter especial, aparece este mensaje de error.
                print("Oops! Please enter a number.")
            except TypeError: #Si el usuario introduce un número decimal, aparece este mensaje. No se genera ninguna cadena, ni con un número decimal ni con uno entero negativo.
                print('Oops! Please enter an integer.')
            else:
                resultado = DNA_chain(length_option)  # cadena de DNA generada.
                if resultado == None: #si se diese el caso de que la función DNA_chain() diese lugar a "None", no se genera ninguna cadena nueva.
                    resultado = '' #El resultado sería una cadena vacía en lugar de "None".
                    print('Generated chain:', resultado)  # se muestra la cadena generada aleatoriamente (en este caso, ninguna).
                    DNA = resultado  # la variable DNA pasa a ser la cadena recién generada, y se muestra al final del menú.
                elif resultado != None: #si la cadena generada no es "None", se muestra de manera normal.
                    print('Generated chain:', resultado)  # se muestra la cadena generada aleatoriamente.
                    DNA = resultado  # la variable DNA pasa a ser la cadena recién generada, y se muestra al final del menú.
        elif(x==2): #opción 2
            now=datetime.datetime.now() #fecha y hora actuales.
            try:
                fichero=str(input('Please, provide a name for a file (a unique identifier will be added to this name automatically): '))+"_dna_string_"+now.strftime("%Y-%m-%d_%H.%M.%S")+".txt" #el usuario escoge cómo desea llamar al archivo y, automáticamente, a dicho nombre se le añade "_dna_string_" y la fecha y hora actuales, para así poder diferenciar entre sí los archivos.
            except NameError: #si el usuario indica un nombre no válido, aparece este mensaje.
                print("Oops! Please enter a valid name.")
            else:
                cadena_guardada=save_chain(fichero) #se guarda la cadena actual (reflejada en la variable DNA) en el fichero cuyo nombre ha escogido el usuario.
                print('The DNA chain has been saved in the file whose name is',cadena_guardada,'in this directory:',os.getcwd()) #se indica el nombre final del archivo y su ubicación.
        elif(x==3): #opción 3
            print('\nList of files, containing DNA chains, in the current directory:')
            list_DNA() #lista de los ficheros que contienen cadenas de DNA.
            try:
                archivo_cargado=str(input('Please, from the above files, indicate the name of the file you want to load: ')) #el usuario escoge, a partir de la lista mostrada, el archivo que desea abrir.
                contenido=load_DNA(archivo_cargado) #se carga el contenido del archivo.
            except FileNotFoundError: #si el usuario indicase un archivo no mostrado en la lista o no existente, aparece este mensaje de error.
                print('Oops! Please enter a valid file name from the list above.')
            except IsADirectoryError: #si el usuario indicase un directorio, aparece este mensaje de error.
                print('Oops! Please enter a valid file name from the list above.')
            else:
                print('\nContent of the file named',archivo_cargado,':',contenido.replace('\n','')) #se imprime el nombre del archivo elegido y su contenido.
                cargar=str(input('Do you wish to work on this DNA chain or not? [y/n]: ')).lower() #se pregunta al usuario si desea trabajar con la secuencia cargada.
                if cargar=='y': #si el usuario dice que sí, la cadena actual se cambia por la cargada.
                    DNA=contenido.replace('\n','')
                    print('The current chain is',DNA) #msnsaje de confirmación.
                else:
                    print('The current chain has not changed.') #mensaje de confirmación.
        elif(x==4): #opción 4
            print('\nList of DNA chains in the current directory:')
            list_DNA() #lista de los ficheros que contienen cadenas de DNA.
        elif(x==5): #opción 5
            print("\n","%s has been removed successfully." %delete_DNA()) #se muestra el nombre del fichero que ha sido eliminado.
        elif(x==6): #opción 6
            def DNA_operations(): #se genera un nuevo menú dentro del menú principal.
                opcion=0
                while opcion<=0 or opcion>6:
                    try:
                        print("----------------------------------------")
                        print("DNA-Toolkit v0.1")
                        print("Operations with DNA chain:")
                        print("1 - Re-Generate DNA chain") #se genera una nueva cadena de DNA, sustituyendo a la anterior.
                        print("2 - Validate DNA chain") #se comprueba que todas las bases de la cadena de DNA actual son correctas (validación).
                        print("3 - Mutate DNA chain") #se introducen mutaciones puntuales en la cadena de DNA actual (las mutaciones pueden ocurrir más de una vez en una posición concreta, y la mutación podría producirse sustituyendo una letra por sí misma).
                        print("4 - Measure frequencies") #se cuenta el número de veces que aparece una base en la cadena de DNA actual, mediante la creación de un diccionario.
                        print("5 - Count subsequences") #se cuenta el número de veces que aparece una subsecuencia en la cadena de DNA actual.
                        print("6 - Back") #se vuelve al menú principal.
                        if DNA=='': #inicialmente, la cadena DNA no tendrá ningún contenido.
                            print('[[There is no DNA chain loaded]]')
                        else:
                            print('[[Current chain:',DNA,"]]") #si hay alguna cadena generada, la variable DNA pasa a ser la cadena de DNA actual (tras ser generada o tras haber mutado otra preexistente).
                        print("----------------------------------------")
                        opcion=eval(input("Please enter a number: ")) #el usuario introduce un número indicando la opción.
                    except NameError: #si el usuario introduce una letra, aparece este mensaje.
                        print("Oops! Please enter a number.")
                    except SyntaxError: #si el usuario introduce un carácter especial, aparece este mensaje.
                        print("Oops! Please enter a number.")
                    else:
                        print("You have selected option",opcion) #se muestra la opción escogida.
                return opcion

            #Función que comprueba la cadena de DNA actual y la valida si todas las bases son correctas.
            def validar_cadena(chain):
                x=0
                while x<len(chain):
                    for base in chain: #para cada base en la cadena de DNA actual
                        if base.upper() in ['A','G','C','T']: #si dicha base es A, G, C o T, esta letra es válida y la función pasa a leer la siguiente base de la cadena.
                             x+=1
                             continue
                        else: #si se encuentra alguna letra no válida, se muestra al usuario que la cadena de DNA no es válida.
                             return 'not valid'
                if x==len(chain):
                    if len(chain)==0: #si el usuario ejecutase esta función sin haber generado antes alguna cadena, aparece este mensaje indicando que genere una cadena de DNA.
                        return 'not valid. Please remember to generate a DNA chain first.'
                    else: #si la cadena no está vacía y todas las letras son válidas, entonces sí se indica que la cadena de DNA actual es válida.
                         return 'valid'
                     
            #Función que inserta tantas mutaciones (puede que más de una vez en una misma posición) como el usuario desee.
            import random
            def random_point_mutater(seq):
                try:
                    coding_dna= list(seq) #la cadena de DNA actual se transforma en una lista.
                    DNA_options= ["A", "G", "T","C"] #se definen las letras por las que se puede sustituir una posición de la cadena.
                    for n in range(opcion_mutacion): #opcion_mutacion es el número de mutaciones que el usuario desea que se introduzcan en la cadena de DNA actual.
                        a=random.randrange(len(seq)) #se genera un número aleatorio entre 0 y la longitud de la cadena de DNA.
                        c=random.randrange(3) #se genera un número aleatorio entre 0 y 3 (incluidos).
                        d=coding_dna[a] #letra que ocupa la posición escogida antes de la mutación.
                        b=DNA_options[c] #se escoge una letra aleatoriamente a partir de las opciones.
                        coding_dna.pop(a) #se elimina el nucleótido presente en la posición escogida aleatoriamente en la cadena de DNA actual.
                        coding_dna.insert(a, b) #se inserta el nucleótido escogido (b) en la posición escogida aleatoriamente (a).
                        back_to_str="".join(coding_dna) #la lista pasa a ser una cadena de nuevo, con la(s) mutación(es) pertinentes.
                        print('Position',a+1,'has been mutated (',d,'->',b,')') #se muestra al usuario en qué posiciones se han producido las mutaciones puntuales y qué letras se han intercambiado.
                    return back_to_str #se devuelve la nueva cadena.
                except ValueError: #si el usuario escoge esta opción sin haber generado antes una cadena de DNA, aparece este mensaje de error.
                    print('Oops! Please remember to generate a DNA chain first.')
                except TypeError: #si el usuario introduce un número decimal, aparece este mensaje de error.
                    print('Oops! Please enter an integer.')
                except UnboundLocalError: #si el usuario introduce un número negativo, aparece este mensaje de error.
                    print('Oops! Please enter a natural number.')

            #Función que cuenta el número de veces que aparece cada base en la cadena de DNA actual.
            def frequencies(string):
                bases=['A','G','T','C'] #bases que se contarán en la cadena de DNA actual.
                dictionary={} #diccionario vacío.
                for b in bases: #para cada base de la cadena, se cuenta el número de veces que ésta aparece en la misma.
                    dictionary[b]=string.count(b)
                return dictionary #se devuelve el diccionario final.

            #Función para contar el número de veces que aparece una subsecuencia en la cadena de DNA actual.
            import re
            def count_subsequences(string):
                try:
                    subseq=(str(input('Please, provide the DNA subseq: '))).upper() #el usuario escoge la subsecuencia a contar.
                except NameError: #si el usuario introduce una subsecuencia no válida, aparece este mensaje de error.
                    print('Oops! Please, enter a subsequence.')
                except AttributeError: #si la cadena de DNA fuese "None", aparece este mensaje de error.
                    print('Oops! Print remember to generate a DNA chain first.')
                else:
                    coincidencias=string.count(subseq) #se cuenta el número de ocurrencias.
                    print(subseq,'appears',coincidencias,'times in',string) #se muestra la subsecuencia y su número de apariciones.
                    for m in re.finditer(subseq,string):
                        print(subseq,'found between the positions',m.start()+1,'and',m.end()) #se muestra entre qué posiciones se encuentra la subsecuencia en la cadena de DNA actual.

            backCode=6
            x=0
            while x!=backCode: #siempre y cuando la opción no sea 6 (atrás), ocurre lo siguiente.
                x=DNA_operations()
                if(x!=backCode):
                    if(x==1): #opción 1.
                        try:
                            length_option=eval(input('Please, provide the length of the DNA chain: ')) #el usuario escoge el número de bases que tendrá la nueva cadena de DNA.
                        except NameError: #si el usuario introduce una letra, aparece este mensaje de error.
                            print("Oops! Please enter a number.")
                        except SyntaxError: #si el usuario introduce un carácter especial, aparece este mensaje de error.
                            print("Oops! Please enter a number.")
                        except TypeError: #Si el usuario introduce un número decimal, aparece este mensaje. No se genera ninguna cadena, ni con un número decimal ni con uno entero negativo.
                            print('Oops! Please enter an integer.')
                        else:
                            resultado = DNA_chain(length_option)  # cadena de DNA generada.
                            if resultado == None: #si se diese el caso de que la función DNA_chain() diese lugar a "None", no se genera ninguna cadena nueva.
                                resultado = '' #El resultado sería una cadena vacía en lugar de "None".
                                print('Generated chain:', resultado)  # se muestra la cadena generada aleatoriamente (en este caso, ninguna).
                                DNA = resultado  #la variable DNA pasa a ser la cadena recién generada, y se muestra al final del menú.
                            elif resultado != None: #si la cadena generada no es "None", se muestra de manera normal.
                                print('Generated chain:', resultado)  # se muestra la cadena generada aleatoriamente.
                                DNA = resultado  #la variable DNA pasa a ser la cadena recién generada, y se muestra al final del menú.
                    elif(x==2): #opción 2.
                        try:
                            print("The DNA chain",DNA,"is",validar_cadena(DNA)) #se muestra si la cadena de DNA actual es válida o no.
                        except TypeError: #si se diese el caso en el que la cadena de DNA fuese "None", aparece este mensaje de error.
                            print('Oops! Please remember to generate a DNA chain first.')
                    elif(x==3): #opción 3.
                        try:
                            opcion_mutacion=eval(input('Please, provide the number of mutations to insert in the DNA chain: ')) #el usuario escoge el número de mutaciones puntuales que desea introducir en la cadena de DNA actual.
                        except NameError: #si el usuario introduce una letra, aparece este mensaje de error.
                            print('Oops! Please enter a number.')
                        except SyntaxError: #si el usuario introduce un carácter especial, aparece este mensaje de error.
                            print('Oops! Please enter a number.')
                        except TypeError: #si el usuario introduce un número decimal, aparece este mensaje y la cadena de DNA actual no cambia.
                            print('Oops! Please enter an integer.')
                        else:
                            print('Previous DNA chain:',DNA) #cadena de DNA anterior.
                            cadena_mutada=random_point_mutater(DNA)
                            if cadena_mutada==None: #si se diese el caso de que la cadena mutada fuese "None", la cadena de DNA actual no se ve cambiada.
                                cadena_mutada=DNA
                                print('Mutated DNA chain: ',cadena_mutada)
                                DNA=cadena_mutada
                            elif cadena_mutada!=None: #si la cadena mutada no fuese "None", la cadena muta de acuerdo a lo indicado por el usuario.
                                print('Mutated DNA chain: ',cadena_mutada) #cadena de DNA tras la(s) mutación(es).
                                DNA=cadena_mutada #la cadena de DNA actual pasa a ser la mutada.
                            print('Please take into account that a certain position may have been mutated more than once. Also, a position may have been mutated with the same letter.') #Aviso aclaratorio.
                    elif(x==4): #opción 4.
                        try:
                            print('DNA frequency',frequencies(DNA)) #se muestran las frecuencias de cada letra de la cadena de DNA actual.
                        except AttributeError: #si la cadena de DNA actual fuese "None", se muestra este mensaje de error.
                            print("Oops! Please remember to generate a DNA chain first.")
                    elif(x==5): #opción 5.
                        try:
                            count_subsequences(DNA) #se muestra el número de veces (y la posición) que aparece una subsecuencia en la cadena de DNA actual.
                        except AttributeError: #si la cadena de DNA actual fuese "None", se muestra este mensaje de error.
                            print('Oops! Please remember to generate a DNA chain first.')

            print("Back to the main menu.") #si el usuario escoge la opción 6, vuelta al menú principal.

print("Exit! Bye Bye!") #si el usuario escoge la opción 7, salida del programa.
            

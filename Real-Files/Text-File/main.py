"""Module providing a function printing python version."""

from os import strerror

try:
    COUNTER = 0
    stream = open('C:/Dev/Python Course/Real-Files/Text-File/text.txt', "rt", encoding='utf-8')
    char = stream.read(1)
    while char != '':
        print(char, end='') # End-of-file (EOF)
        COUNTER += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", COUNTER)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno)) # End-of-file (EOF)
    # End-of-file (EOF)
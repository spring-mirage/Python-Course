"""Module providing a function printing python version."""

from os import strerror

try:
    counter = 0
    stream = open('C:/Dev/Python Course/Real-Files/Text-File/text.txt', "rt", encoding='utf-8')
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno)) # End-of-file (EOF)
    # End-of-file (EOF)
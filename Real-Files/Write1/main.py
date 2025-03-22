from os import strerror

try:
    file = open('C:/Dev/Python-Course/Real-Files/Write1/newtext.txt', 'wt', encoding='utf-8')
    for i in range(10):
        file.write("línea #" + str(i+1) + "\n")
    file.close()
    print("El archivo se ha escrito correctamente")
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
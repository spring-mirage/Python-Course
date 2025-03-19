try:
    stream = open("C:\Users\User\Desktopile.txt", "rt")
    # El procesamiento va aquí.
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)


#stream = open(file, mode = 'r', encoding = None)


try:
    stream = open("C:/Users/User/Desktop/file.txt", "rt")
    # El procesamiento va aquí.
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)


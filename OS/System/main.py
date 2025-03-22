import os

returned_value = os.system("mkdir my_first_directory")
if(returned_value == 0):
    print("Directorio creado", returned_value)
else:
    print("Error al crear el directorio", returned_value)
    
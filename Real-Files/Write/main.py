from os import strerror

try:
	file = open('C:/Dev/Python Course/Real-Files/Write/newtext.txt', 'wt', encoding='utf-8') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
	print("Archivo creado con éxito.")
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
    
from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('C:/Dev/Python Course/Real-Files/Text-File/text.txt', "rt", encoding='utf-8'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo:", ccnt)
	print("Líneas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
    
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('C:/Dev/Python Course/Real-Files/Bytearray-Write/file.bin', 'wb')
    bf.write(data)
    bf.close()
    print("Se ha escrito el archivo binario")
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

# Ingresa aquí el código que lee los bytes del stream.
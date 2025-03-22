from os import strerror

try:
    binary_file = open('C:/Dev/Python Course/Real-Files/Bytearray-Write/file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
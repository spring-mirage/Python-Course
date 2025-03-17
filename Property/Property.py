class Sample:
    gamma = 0 # Variable de clase.
    def __init__(self):
 
        self.alpha = 1 # Variable de instancia.
        self.__delta = 3 # Instancia de variable privada.
 
 
obj = Sample()
obj.beta = 2 # Otra variable de instancia (que existe solo dentro de la instancia "obj".)
print(obj.__dict__)
class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("Mi nombre es " + self.name + " y estoy viviendo en " + Sample.__module__)
 
 
obj = Sample()
obj.myself()



#new
class Snake:
    pass
 
 
class Python(Snake):
    pass
 
 
print(Python.__name__, 'es una', Snake.__name__)
print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__)
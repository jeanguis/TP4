class Cola:
    def __init__(self):
        self.items=[]

    def encolar(self, x):
        self.items.append(x)
    
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")

    def es_vacia(self):
        return self.items == []


t=Cola()
t.encolar(1)
t.encolar(2)
t.encolar(3)

while not t.es_vacia():
    print t.desencolar()
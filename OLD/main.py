import argparse
#mport classPila
from MCProgram import MCProgram
class Pila:
	def __init__(self):
		self.items=[]
	def apilar(self, x):
			self.items.append(x)

	def desapilar(self):
		try:
			return self.items.pop()
		except IndexError:
			raise ValueError("La pila")

	def es_vacia(self):
		return self.items == []

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

command = ["<", ">", "+", "-", ".","[","]"]
struct = Pila()
program = Cola()

def file_open(file):
	try:
		file = open(file)
	except IOError:
		return 0
	process_file(file)	

def process_file(file):
	currentColas = program

	for line in file:
		for char in line:
			if char in command:
				if char == "[":
					struct.apilar("1")
					currentColas = Cola()
				elif char == "]":
					struct.desapilar()
					program.encolar(currentColas)
					currentColas = program
				else:
					currentColas.encolar(char)

	if not struct.es_vacia():
		print "Format error"
		exit()



def main():
    parser = argparse.ArgumentParser(description='Interprete de codigo MataCerebros')
    parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')
    parser.add_argument('-d', '--debug', action='store_true', help='modo debug')
    args = parser.parse_args()

    nombre_archivo = args.archivo
    modo_debug = args.debug

    file_open("1.mc")

    #cinta_size = 30000
   # cinta = [0 for i in xrange(1,cinta_size)]
   


    M=MCProgram()
    M.process_action(program)
    print M
   # celdaopen=False;
   # for t in list("+++>++>++.++.+"):
   #     if t == "[":
   #         celdaopen=True
   #    if t == "]":
   #         celdaopen=False
   #     M.command(t)
    #print str(celda)
    #print type(M)
    #print M



main()
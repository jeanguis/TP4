import argparse
from Listas import *
from MataCerebros import MataCerebros

#We will put those in Class Matacerebros after, here for tests.
def file_open(file):
	try:
		file = open(file)
	except IOError:
		return 0
	process_file(file)	


programBuffer = Cola()
command = ["<", ">", "+", "-", ".","[","]"]
struct = Pila()

#We will put those in Class Matacerebros after, here for tests.
def process_file(file):
	currentColas = programBuffer

	for line in file:
		for char in line:
			if char in command:
				if char == "[":
					struct.apilar("1")
					currentColas = Cola()
				elif char == "]":
					struct.desapilar()
					programBuffer.encolar(currentColas)
					currentColas = programBuffer
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
    M=MataCerebros()
    M.process_action(programBuffer)
    print M

main()
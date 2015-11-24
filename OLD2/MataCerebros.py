from Listas import *

class MataCerebros(object):

	def __init__(self, cintaSize = 30000):
		#Here we need to implement ListeDouble (cf. Listas.py)
		cintaList = ListaDoble()
		for i in xrange(1,cintaSize):
			cintaList.append(0)
		self.currentCelda = 0
		self.actionDict = {"+": self.add, "-": self.remove, ">": self.up, "<": self.down, ".": self.printascii };

	

	def add(self):
		self.celda[self.currentCelda] += 1
		return self.celda[self.currentCelda]

	def remove(self):
		self.celda[self.currentCelda] -= 1

	def up(self):
		self.currentCelda += 1
		return self.currentCelda
	def down(self):
		self.currentCelda -= 1
		return self.currentCelda

	def printascii(self):
		#print chr(self.celda[self.currentCelda])
		print self.celda[self.currentCelda]

	def command(self,action):
		self.actionDict[action]()

	def __str__(self):
		return str(self.celda)

	def process_action(self,colas, firstCelda = 0):
		#print self
		while not colas.es_vacia():
			action=colas.desencolar()
			#print action
			if type(action) is str:
				#WORK GREAT
				self.command(action)
			else:
				#PART OF THE PROBLEM
				cicleCelda = self.currentCelda
				cicleCola = action
				while not self.celda[0] == 0:
					newCola = Cola()
					while not cicleCola.es_vacia():
						cAction = cicleCola.desencolar()
						newCola.encolar(cAction)
						self.command(cAction)
					cicleCelda = newCola


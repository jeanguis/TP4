from Listas import *

class MataCerebros(object):

	def __init__(self, cintaSize = 300000):
		self.cintaList = ListaDoble()
		for i in xrange(1,cintaSize):
			self.cintaList.append(0)
		self.currentCelda = self.cintaList.head
		self.actionDict = {"+": self.add, "-": self.remove, ">": self.up, "<": self.down, ".": self.printascii };


	def add(self):
		if self.currentCelda: 
			self.currentCelda.dato +=1
			return self.currentCelda.dato

	def remove(self):
		if self.currentCelda: 
			self.currentCelda.dato -=1
			return self.currentCelda.dato

	def up(self):
		self.currentCelda=self.currentCelda.prox
		return self.currentCelda

	def down(self):
		self.currentCelda=self.currentCelda.prev
		return self.currentCelda

	def printascii(self):
		#print chr(self.currentCelda.dato)
		print self.currentCelda.dato

	def command(self,action):
		if action in self.actionDict: 
			self.actionDict[action]()

	def __str__(self):
		self.cintaList.show()
		return ""

	def process_action(self,colas, firstCelda =0):
		while not colas.es_vacia():
			#raw_input()
			action=colas.desencolar()
			print "ACTION:",action
			if type(action) is str:
				self.command(action)
			else:
				cicleCelda = self.currentCelda
				cicleCola = action
				while not cicleCelda.dato == 0:
					newCola = Cola()
					while not cicleCola.es_vacia():
						newAction = cicleCola.desencolar()
						self.command(newAction)
						newCola.encolar(newAction)
					cicleCola=newCola


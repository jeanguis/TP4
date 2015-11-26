from Listas import *

class MataCerebros(object):

	def __init__(self, cintaSize = 10):
		self.cintaList = ListaDoble()
		for i in xrange(1,cintaSize):
			self.cintaList.append(0)
		self.currentCelda = self.cintaList.head.prox.prox
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
		if self.currentCelda.prox:
			self.currentCelda=self.currentCelda.prox
		else:
			self.cintaList.append(0)
			self.currentCelda=self.currentCelda.prox
		return self.currentCelda

	def down(self):
		if self.currentCelda.prev:
			self.currentCelda=self.currentCelda.prev
		else:
			print "VALOR:",self.currentCelda.dato
			print "VALOR NEXT:",self.currentCelda.prox.dato
			print "VALOR NEXT2:",self.currentCelda.prox.prox.dato
			print "VALOR NEXT3:",self.currentCelda.prox.prox.prox.dato
			print self
			exit()
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
			if type(action) is str:
				self.command(action)
			else:
				cicleCelda = self.currentCelda
				#cicleCola = Cola()
				#while not action.es_vacia():
				#	cicleCola.encolar(action.desencolar())
				cicleCola = action
				while not cicleCelda.dato == 0:
					newCola = Cola()
					while not cicleCola.es_vacia():
						newAction = cicleCola.desencolar()
						self.command(newAction)
						newCola.encolar(newAction)
					cicleCola=newCola


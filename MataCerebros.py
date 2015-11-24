import Listas

class MataCerebros(object):

	def __init__(self):
		self.celda = [0 for i in xrange(1,20)]
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
		print chr(self.celda[self.currentCelda])

	def command(self,action):
		self.actionDict[action]()

	def __str__(self):
		return str(self.celda)

	def process_action(self,colas):
		#print self
		while not colas.es_vacia():
			action=colas.desencolar()
			print action
			if type(action) is str:
				self.command(action)
			else:
				L=[]
				T=Cola()
				while not action.es_vacia():
					L.append(action.desencolar());
					
					for i in xrange(1,2):
						for l in L:
							T.encolar(l)
						
					self.process_action(T)	

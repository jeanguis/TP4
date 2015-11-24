class Nodo(object):
	def __init__(self, dato=None, prox = None):
		self.dato = dato
		self.prox = prox
	
	def __str__(self):
		return str(self.dato)

class ListaEnlazada(object):
	def __init__(self):
		self.prim = None
		self.len = 0

		def pop(self, i = None):
			if i is None:
				i = self.len - 1

			if not (0 <= i < self.len):
				raise IndexError("Indice fuera de rango")

			if i == 0:
				dato = self.prim.dato
				self.prim = self.prim.prox
			else:
				n_ant = self.prim
				n_act = n_ant.prox
				for pos in xrange(1, i):
					n_ant = n_act
					n_act = n_ant.prox
				dato = n_act.dato
				n_ant.prox = n_act.prox
			self.len -= 1
			return dato

	def remove(self, x):
		if self.len == 0:
			raise ValueError("Lista vacia")
		elif self.prim.dato == x:
			self.prim = self.prim.prox
		else:
			n_ant = self.prim
			n_act = n_ant.prox
			while n_act != None and n_act.dato != x:
				n_ant = n_act
				n_act = n_ant.prox
			if n_act == None:
				raise ValueError("El valor no esta en la lista.")
			else:
				n_ant.prox = n_act.prox
		self.len -= 1
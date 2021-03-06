class Nodo(object):
	def __init__(self, dato=None, prox = None, prev = None):
		self.dato = dato
		self.prox = prox
		self.prev = prev
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
			for pos in xrange(1,i):
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

	def insert(self, i, x):
		if (i > self.len) or (i < 0):
			raise IndexError("Posicion invalida")
		
		nuevo = Nodo(x)
		
		if i == 0:
			nuevo.prox = self.prim
			self.prim = nuevo
		else:
			n_ant = self.prim
			for pos in xrange(1,i):
				n_ant = n_ant.prox
			nuevo.prox = n_ant.prox
			n_ant.prox = nuevo
		self.len += 1

	def append(self, x):
		self.insert(self.len, x)

	def __iter__(self):
		return _IteradorListaEnlazada(self.prim)

class _IteradorListaEnlazada(object):
	def __init__(self, prim):
		self.actual = prim
	
	def prox(self):
		if self.actual == None:
			raise StopIteration("No hay mas elementos en la lista")
		dato = self.actual.dato
		self.actual = self.actual.prox
		return dato

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

class ListaDoble(object):
 
 	def __init__(self):
		self.head = None
		self.tail = None
 
	def append(self, dato):
		new_node = Nodo(dato, None, None)
		if self.head is None:
			self.head = self.tail = new_node
		else:
			new_node.prev = self.tail
			new_node.prox = None
			self.tail.prox = new_node
			self.tail = new_node
 
	def remove(self, node_value):
		current_node = self.head
 
		while current_node is not None:
			if current_node.dato == node_value:
                # if it's not the first element
				if current_node.prev is not None:
					current_node.prev.prox = current_node.prox
					current_node.prox.prev = current_node.prev
				else:
					# otherwise we have no prev (it's None), head is the prox one, and prev becomes None
					self.head = current_node.prox
					current_node.prox.prev = None
 
			current_node = current_node.prox
 
	def show(self):
		print "Show list dato:"
		current_node = self.head
		while current_node is not None:
			#print current_node.prev.dato if hasattr(current_node.prev, "dato") else None,
			print current_node.dato,
			#print current_node.prox.dato if hasattr(current_node.prox, "dato") else None
 
			current_node = current_node.prox
		print ""

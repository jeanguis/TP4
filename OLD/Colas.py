#! /usr/bin/env python
#encoding: latin1
class Cola:
	def __init__(self):
		self.items=[]

	def encolar(self, x):
		self.items.append(x)
	
	def desencolar(self):
		try:
			return self.items.pop(0)
		except:
			raise ValueError("La cola está vacia")

	def es_vacia(self):
		return self.items == []
import nodos
class cola1:
	def __init__(self):
		self.cabeza=None
		self.sig=None
		self.first=None
		self.tam=0

	def push(self,info):
		c=nodos.nodo()
		c.setinfo(info)
		if (self.cabeza==None):
			self.tam=0
			self.first=c
			self.cabeza=c
			self.tam=self.tam+1
		else:
			self.cabeza.setsig(c)
			self.cabeza=c
			self.tam=self.tam+1
	def pop(self):
		if (self.first==None):
			return "vacia"
		else:
			self.tam = self.tam-1
			if (self.first==self.cabeza):
				val = self.first.getinfo()
				self.first=None
				self.cabeza=None
				return val
			else:
				val = self.first.getinfo()
				self.first=self.first.getsig()
				return val

	def mostrar(self):
		c = self.first
		for x in range(0,self.tam):
			print (str(c.getinfo()))
			c=c.getsig()








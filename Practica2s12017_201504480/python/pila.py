import nodos
class pila1:
	def __init__(self):
		self.cabeza=None
		self.tam = 0

	def push(self,informa):
		nodotem = nodos.nodo()
		nodotem.setinfo(informa)
		nodotem.setsig(self.cabeza)
		self.cabeza=nodotem
		self.tam=self.tam+1

	def pop(self):
		if (self.cabeza==None):
			return "vacia"
		elif (self.tam==1):
			nodotem = self.cabeza.getinfo()
			self.cabeza=None
			return nodotem
		else:
			nodotem = self.cabeza.getinfo()
			self.cabeza = self.cabeza.getsig()
			return nodotem

		

	def mostrar(self):
		nodomost = self.cabeza
		while (nodomost!= None):
			print ("valor: ",nodomost.getinfo())
			nodomost = nodomost.getsig()


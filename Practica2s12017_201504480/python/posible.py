import nodosd
class listad1:

	def __init__(self):
		self.cl =None
		self.cdir = None

	def agregar (self,nombre,tipo):

		nodoinfo = nodosd.nodosd1()
		nodoinfo.setinfo(nombre)
		if (self.cl ==None and self.cdir ==None):
			nodoletra= nodosd.nodosd1()
			nodoletra.setinfo(nombre[0])
			nododir = nodosd.nodosd1()
			nododir.setinfo(tipo)
			#LETRA CON INFO 
			nodoletra.setsig(nodoinfo)
			nodoinfo.setante(nodoletra)
			#INFO CON DIR
			nodoinfo.setarriba(nododir)
			nododir.setabajo(nodoinfo)
			#agreagamos
			self.cl=nodoletra
			self.cdir=nododir
		else:
			condl =False
			nodotemletra = self.cl
			
			while (nodotemletra!=None):
				if (str(nodotemletra.getinfo())==nombre[0]):
					nodoletraen = nodotemletra

					condl = True
				nodotemletra = nodotemletra.getabajo()
			condl2 =False
			nodotemdir= self.cdir
			while (nodotemdir!=None):
				if (nodotemdir.getinfo()==tipo):
					nodotemdiren = nodotemdir
					condl2 = True
				nodotemdir = nodotemdir.getsig()

			if (condl==False and condl2==False):
					nodoletra= nodosd.nodosd1()
					nodoletra.setinfo(nombre[0])
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombre[0],nodoletra)
					letra = nombre[0]
					nodotem = self.cl
					while (nodotem!=None):
						if (ord (letra[0]) < ord(str(nodotem.getinfo()))):
							print ("menor")
							if (nodotem.getarriba()==None):
								#print ("arriba none")
								nodoletra.setarriba(None)
								nodoletra.setabajo(nodotem)
								nodotem.setarriba(nodoletra)
								if (self.cl == nodotem):
									self.cl = nodoletra
								
							else:
								nodoletra.setarriba(nodotem.getarriba())
								nodoletra.setabajo(nodotem)
								nodotem.getarriba().setabajo(nodoletra)
								nodotem.setarriba(nodoletra)
							break
						elif (nodotem.getabajo()==None):
							print("ultiminodo")
							nodotem.setabajo(nodoletra)
							nodoletra.setarriba(nodotem)
							nodoletra.setabajo(None)
							break
						nodotem = nodotem.getabajo()
				#agregar dir ordenada
					nododirn= nodosd.nodosd1()
					nododirn.setinfo(tipo)
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombre[0],nodoletra)
					letra = nombre[0]
					nodotemd = self.cdir
					while (nodotemd!=None):
						if (tipo < nodotemd.getinfo()):
							print ("menor")
							if (nodotemd.getante()==None):
								#print ("arriba none")
								nododirn.setante(None)
								nododirn.setsig(nodotemd)
								nodotemd.setante(nododirn)
								if (self.cdir == nodotemd):
									self.cdir = nododirn
								
							else:
								nododirn.setante(nodotemd.getante())
								nododirn.setsig(nodotemd)
								nodotemd.getante().setsig(nododirn)
								nodotemd.setante(nododirn)
							break
						elif (nodotemd.getsig()==None):
							print("ultiminodo")
							nodotemd.setsig(nododirn)
							nododirn.setante(nodotemd)
							nododirn.setsig(None)
							break
						nodotemd = nodotemd.getsig()
					nodoletra.setsig(nodoinfo)
					nodoinfo.setante(nodoletra)
					#INFO CON DIR
					nodoinfo.setarriba(nododirn)
					nododirn.setabajo(nodoinfo)

			if(condl==True and condl2==False):
					#agregar nuevo nodo
				#agregar dir ordenada
					nododirn= nodosd.nodosd1()
					nododirn.setinfo(tipo)
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombre[0],nodoletra)
					letra = nombre[0]
					nodotemd = self.cdir
					while (nodotemd!=None):
						if (tipo < nodotemd.getinfo()):
							print ("menor")
							if (nodotemd.getante()==None):
								#print ("arriba none")
								nododirn.setante(None)
								nododirn.setsig(nodotemd)
								nodotemd.setante(nododirn)
								if (self.cdir == nodotemd):
									self.cdir = nododirn
								
							else:
								nododirn.setante(nodotemd.getante())
								nododirn.setsig(nodotemd)
								nodotemd.getante().setsig(nododirn)
								nodotemd.setante(nododirn)
							break
						elif (nodotemd.getsig()==None):
							print("ultiminodo")
							nodotemd.setsig(nododirn)
							nododirn.setante(nodotemd)
							nododirn.setsig(None)
							break
						nodotemd = nodotemd.getsig()

					#metodo encontrar la letra ya existente
					letra = nombre[0]
					nodotem = self.cl
					while (nodotem!=None):
						if ((letra[0]) ==(str(nodotem.getinfo()))):
							print ("letra repetida",str(nodotem.getinfo()))
							break
						nodotem = nodotem.getabajo()

					nodoinfo.setarriba(nododirn)
					nododirn.setabajo(nodoinfo)
					#buscar nodo exacto de letra a enlazar
					if (nododirn.getsig()==None):
						nodocolumnaa = nodocolumnadir(nodotem,tipo)
						nodoinfo.setsig(None)
						nodocolumnaa.setsig(nodoinfo)
						nodoinfo.setante(nodocolumnaa)
					else:
						nodocolumnaa = nodocolumnadir(nodotem,tipo)
						nodoinfo.setsig(nodocolumnaa)
						nodoinfo.setante(nodocolumnaa.getante())
						nodocolumnaa.getante().setsig(nodoinfo)
						nodocolumnaa.setante(nodoinfo)


				




					
		


		


	def mostrarl(self):
		nodotem = self.cl
		while (nodotem!=None):
			print (nodotem.getinfo())
			#print (nodotem.getinfo(),"----",nodotem.getsig().getinfo())
			nodotem= nodotem.getabajo()

	def mostrardir(self):
		nodotem = self.cdir
		while (nodotem!=None):
			print (nodotem.getinfo())
			nodotem= nodotem.getsig()

def nodocolumnadir(nodotem,tipo):
	nodoenviar = nodosd.nodosd1()
	nodoenviar = nodotem
	tem = nodotem.getsig()
	while (tem!=None):
		temcolum = tem
		#print ("valor arriba tem",temcolum.getinfo())
		while (temcolum.getarriba()!=None):
			temcolum = temcolum.getarriba()
			#print ("valor arriba temcolum",temcolum.getinfo())
		if(tipo < temcolum.getinfo()):
			nodoenviar= tem
			break
		if (tem.getsig()==None):
			nodoenviar = tem


		tem=tem.getsig()
	return nodoenviar

			











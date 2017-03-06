import nodosd
import listasimple
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
					nodocolumnaa = nodocolumnadir(nodotem,tipo)
					if (nodocolumnaa.getsig()==None and cabeceral(nodocolumnaa).getinfo()< tipo ):

						nodocolumnaa = nodocolumnadir(nodotem,tipo)
						print (nodoinfo.getinfo(),"columa a enlazar principio",nodocolumnaa.getinfo())
						nodoinfo.setsig(None)
						nodocolumnaa.setsig(nodoinfo)
						nodoinfo.setante(nodocolumnaa)
					else:
						nodocolumnaa = nodocolumnadir(nodotem,tipo)
						print (nodoinfo.getinfo(),"columa a enlazar lado lado ",nodocolumnaa.getinfo())
						nodoinfo.setsig(nodocolumnaa)
						nodoinfo.setante(nodocolumnaa.getante())
						nodocolumnaa.getante().setsig(nodoinfo)
						nodocolumnaa.setante(nodoinfo)
			if (condl==False and condl2==True):
					nodoletra= nodosd.nodosd1()
					nodoletra.setinfo(nombre[0])
					#metodo de la posicion a agregar letra
					#nodoletratemanteriorm(nombre[0],nodoletra)

					letra = nombre[0]
					nodotem = self.cl



					while (nodotem!=None):
						print ("menor:    -",nodotem.getinfo())
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
					nodoletra.setsig(nodoinfo)
					nodoinfo.setante(nodoletra)

					#buscar nodo exacto de letra a enlazar
					nodotem = self.cdir
					while (nodotem!=None):
						if (tipo ==(str(nodotem.getinfo()))):
							print ("tipo repetido",str(nodotem.getinfo()))
							break
						nodotem = nodotem.getsig()

					nodocolumnaa = nodofilaletra(nodotem,nombre[0])

					if (nodocolumnaa.getabajo()==None and cabeceradir(nodocolumnaa).getinfo()<nombre[0]):
						print (nodoinfo.getinfo(),"columa a enlazar principio",nodocolumnaa.getinfo())
						nodoinfo.setabajo(None)
						nodocolumnaa.setabajo(nodoinfo)
						nodoinfo.setarriba(nodocolumnaa)
					else:
						print (nodoinfo.getinfo(),"columa a doble",nodocolumnaa.getinfo())
						nodoinfo.setabajo(nodocolumnaa)
						nodoinfo.setarriba(nodocolumnaa.getarriba())
						nodocolumnaa.getarriba().setabajo(nodoinfo)
						nodocolumnaa.setarriba(nodoinfo)

			if (condl==True and condl2==True):
				nodotem = self.cdir
				nodotemdir = nodosd.nodosd1()
				while (nodotem!=None):
					if (tipo ==(str(nodotem.getinfo()))):
						print ("tipo repetido",str(nodotem.getinfo()))
						nodotemdir = nodotem
						break
					nodotem = nodotem.getsig()

					#nodocolumnaa = nodofilaletra(nodotem,nombre[0])
				letra = nombre[0]
				nodotem = self.cl
				nodotemletra = nodosd.nodosd1()
				while (nodotem!=None):
					if ((letra[0]) ==(str(nodotem.getinfo()))):
						print ("letra repetida",str(nodotem.getinfo()))
						nodotemletra=nodotem
						break
					nodotem = nodotem.getabajo()

				#print (nodotemletra.getinfo(),"-@-",nodotemdir.getinfo())
				#buscar nodo exacto de letra a enlazar
				#nodocolumnaa = nodocolumnadir(nodotem,tipo)
				nodoactual = nodoactualcondir(nodotemdir,nombre)
				tempnodoa = nodoactual
				print (tempnodoa.getinfo())
				while (tempnodoa.getsig()!=None):
					tempnodoa=tempnodoa.getatras()

				tempnodoa.setatras(nodoinfo)
				nodoinfo.setadelante(tempnodoa)





				




					
	def bletral (self, parametro):
		nodotem = self.cl
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodoadentro.getinfo()[0]):

						print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()
		#listenv.mostrar()
		#gk =str(listenv.tam())
		return str(fc)
	def bletral1 (self, parametro,con):
		nodotem = self.cl
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodoadentro.getinfo()[0]):

						#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()
		gk =str(listenv.buscarp(con))
		return gk

###
	def bletraldir (self, parametro):
		nodotem = self.cdir
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodotem.getinfo()):
						#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()	
		#listenv.mostrar()
		#gk =str(listenv.tam())
		return str(fc)
	def bletraldir1 (self, parametro,con):
		nodotem = self.cdir
		listenv = listasimple.ListaS()
		fc =0
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					if(parametro==nodotem.getinfo()):
						#print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
						fc=fc+1
						listenv.enlistar(nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()
		gk =str(listenv.buscarp(con))
		return gk



##3
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
	def mostrartvarl(self):
		nodotem = self.cl
		while (nodotem!=None):
			dm = nodotem
			dm = dm.getsig()
			while (dm!=None):
				print (nodotem.getinfo(),"...",dm.getinfo())
				dm = dm.getsig()
				
			nodotem = nodotem.getabajo()
	def mostrartvarl2(self):
		nodotem = self.cdir
		while (nodotem!=None):
			dm = nodotem
			dm = dm.getabajo()
			while (dm!=None):
				print (nodotem.getinfo(),"...",dm.getinfo())
				dm = dm.getabajo()
				
			nodotem= nodotem.getsig()

	def mostrartodoh(self):
		nodotem = self.cl
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getsig()
			nodotem = nodotem.getabajo()
				

	def mostrartodov(self):
		nodotem = self.cdir
		while (nodotem!=None):
			nodotemh = nodotem
			while (nodotemh!=None):
				nodoadentro = nodotemh
				while(nodoadentro!=None):
					print ("cabecera",nodotem.getinfo(),"--primernodo--",nodotemh.getinfo(),"--info--",nodoadentro.getinfo())
					nodoadentro = nodoadentro.getatras()
				nodotemh = nodotemh.getabajo()
			nodotem = nodotem.getsig()	

def nodocolumnadir(nodotem,tipo):
	nodoenviar = nodosd.nodosd1()
	nodoenviar = nodotem
	tem = nodotem.getsig()
	while (tem!=None):
		temcolum = tem
		print ("valor arriba tem",temcolum.getinfo())
		while (temcolum.getarriba()!=None):
			temcolum = temcolum.getarriba()
			print ("valor arriba temcolum",temcolum.getinfo())
		if(tipo < temcolum.getinfo()):
			nodoenviar= tem
			break
		if (tem.getsig()==None):
			print("nonoe","--",tem.getinfo())
			nodoenviar = tem


		tem=tem.getsig()
	return nodoenviar
def cabeceral(nodotem):
	nodoenviar = nodosd.nodosd1()
	tem =nodotem.getarriba()
	nodoenviar = tem
	while (tem!=None):
		nodoenviar = tem
		tem = tem.getarriba()
	return nodoenviar

def cabeceradir(nodotem):
	nodoenviar = nodosd.nodosd1()
	tem =nodotem.getante()
	nodoenviar = tem
	while (tem!=None):
		nodoenviar = tem
		tem = tem.getante()
	return nodoenviar




def nodofilaletra(nodotem,letra):
	nodoenviar = nodosd.nodosd1()
	nodoenviar = nodotem
	tem = nodotem.getabajo()
	while (tem!=None):
		temcolum = tem
		print ("valor arriba tem",temcolum.getinfo())
		while (temcolum.getante()!=None):
			temcolum = temcolum.getante()
			#
			print ("valor letra abajo",temcolum.getinfo()[0])
		if(letra[0] < str(temcolum.getinfo())[0]):
			nodoenviar= tem
			break
		if (tem.getabajo()==None):
			nodoenviar = tem


		tem=tem.getabajo()
	return nodoenviar

def nodoactualcondir(nodotemdir,nombre):
	temp = nodotemdir
	while (temp!=None ):
		print("copiado",temp.getinfo(),"-- nombre:--- ",nombre[0])
		if(temp.getinfo()[0] ==nombre[0]):
			break
		temp = temp.getabajo()

	return temp















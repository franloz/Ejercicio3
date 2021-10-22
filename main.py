class Serie:
    def __init__(self,titulo="", numTemp=3, entregado=False, genero="", creador=""):
        self.titulo = titulo
        self.numTemp = numTemp
        self.entregado = entregado
        self.genero = genero
        self.creador = creador


    def getTitulo(self):
        return self.titulo

    def getNumTemp(self):
        return self.numTemp

    def getTitulo(self):
        return self.titulo

    def getGenero(self):
        return self.genero

    def getCreador(self):
        return self.creador


    def setTitulo(self,a):
        self.titulo=a

    def setNumTemp(self,a):
        self.numTemp=a

    def selfGenero(self,a):
        self.genero=a

    def setNumTemp(self,a):
        self.numTemp=a

    def setCreador(self,a):
        self.creador=a

    def toString(self):
        print ("Titulo: " + str(self.titulo) + ", numTemp: " + str(self.numTemp) +", entregado: " + str(self.entregado) +", genero: " + str(self.genero) + ", creador: " + str(self.creador))


class Videojuego:
    def __init__(self, titulo="", horasEstimadas=10, entregado=False, genero="", compania=""):
        self.titulo = titulo
        self.horasEstimadas = horasEstimadas
        self.entregado = entregado
        self.genero = genero
        self.compania = compania

    def getTitulo(self):
        return self.titulo

    def getHorasEstimadas(self):
        return self.horasEstimadas

    def getGenero(self):
        return self.genero

    def getCompania(self):
        return self.compania


    def setTitulo(self,a):
        self.creador = a

    def setHorasEstimadas(self,a):
        self.horasEstimadas = a

    def setGenero(self,a):
        self.genero = a

    def setCompania(self,a):
        self.compania = a

series=[]
videojuegos=[]
series.append(Serie("Superman",4,True,"accion","DC"))
series.append(Serie("Batman",6,True,"accion","DC"))
series.append(Serie("Azuleta",2,True,"terror","Galvini"))
series.append(Serie("Jurasico",1,False,"cienciaficcion","Paramount"))
series.append(Serie("El bueno",2,False,"western","Clint"))

videojuegos.append(Videojuego("Lol",4,True,"accion","Game"))
videojuegos.append(Videojuego("ClashRoyal",18,True,"estrategia","STG"))
videojuegos.append(Videojuego("Mir4",4,False,"terror","RaR"))
videojuegos.append(Videojuego("JurasicWorld",7,False,"cienciaficcion","Epic"))
videojuegos.append(Videojuego("Shooter",2,False,"punteria","Fer"))

seriesentregadas=0
juegoentregados=0

serieMasTemporadas = Serie()
juegoMasHoras = Videojuego()

for s in series:
    if s.entregado:
        seriesentregadas=seriesentregadas+1
        print(s.titulo)
        if s.numTemp > serieMasTemporadas.numTemp:
            nombreMasTemporadas=s.titulo

print("Total de series entregadas: " + repr(seriesentregadas))
print("Serie con más temporadas: " + repr(nombreMasTemporadas))

for j in videojuegos:
    if j.entregado:
        juegoentregados=juegoentregados+1
        print(j.titulo)
        if j.horasEstimadas > juegoMasHoras.horasEstimadas:
            nombreMasHoras=j.titulo

print("Total de juegos entregadas: " + repr(juegoentregados))
print("Juego con más horas: " + repr(nombreMasHoras))


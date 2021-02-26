class nodoMat():

    def __init__(self, f, c, v):
        self.valor = v
        self.fila = f
        self.columna = c
        self.siguiente = None
# class nodoMat():

#     def __init__(self, g, f):
#         self.grupo = g
#         self.fila = f
#         self.siguiente = None

class listaMatriz():

    def __init__(self):
        self.inicio = None

    def agregarValor(self, fil, col, val):
        temp = nodoMat(fil, col, val)
        
        if self.inicio == None:
            self.inicio = temp
        else:
            aux = self.inicio
            while True:
                if aux.siguiente == None:
                    break
                else: 
                    aux = aux.siguiente
            aux.siguiente = temp

    def busquedaPos(self, f, c):
        aux = self.inicio
        while True:
            if aux.fila == f and aux.columna == c:
                return aux.valor
            if aux.siguiente == None:
                break
            else: 
                aux = aux.siguiente
        return None
        
# <matriz n="4" m="4">
# <dato x="1" y="1">2</dato>
n = 3
m = 3

objLM = listaMatriz()
objLM.agregarValor(3,3,0)
objLM.agregarValor(1,1,15)
objLM.agregarValor(2,1,18)
objLM.agregarValor(2,2,19)
objLM.agregarValor(2,3,0)
objLM.agregarValor(3,1,1)
objLM.agregarValor(1,2,16)
objLM.agregarValor(1,3,0)
objLM.agregarValor(3,2,9)

for i in range(0, n):
    p = ""
    for j in range(0, m):
        p = p + str(objLM.busquedaPos(i+1, j+1)) + "\t"
    print(p)


objLP = listaMatriz()

for i in range(0, n):
    #p = ""
    for j in range(0, m):
        #p = p + str(objLM.busquedaPos(i+1, j+1)) + "\t"
        val = 0
        if objLM.busquedaPos(i+1, j+1) > 0:
            val = 1
        objLP.agregarValor(i+1, j+1, val)
    #print(p)
print()
print()
for i in range(0, n):
    p = ""
    for j in range(0, m):
        p = p + str(objLP.busquedaPos(i+1, j+1)) + "\t"
    print(p)


grp = []
contG = 1
for fil in range(0, n-1): #0
    #Validacion de existencia en la lista
    seCompara = True
    #print("fil estatica")
    if len(grp) > 0:
        for gr in grp: #[[1,1],[1,2]]
            if gr[1] == fil+1:
                seCompara = False

    if seCompara:
        grp.append([contG, fil+1])
        for filC in range(fil+1, n): #1
            #print("fila compara")
            esIgual = True
            for col in range (0,m):
                #print("col compara")
                if not (objLP.busquedaPos(fil+1, col+1) == objLP.busquedaPos(filC+1, col+1)):
                    esIgual = False
            if esIgual:
                grp.append([contG, filC+1])
        contG += 1
if len(grp) > 0:
    seAlmacena = True
    for gr in grp: #[[1,1],[1,2]]
        #print("ultima fila")
        if gr[1] == n:
            seAlmacena = False
    if seAlmacena:
        grp.append([contG, n])
print()
print(grp)


class Nodo:
    def __init__(self, elemento=None):
        self.__elemento = elemento #atributo que tendra el nodo
        self.pSig = None #puntero que unira los nodos, cuando se haga la lista

    def Obtener_Elemento(self):    
        return self.__elemento


class Lista:
    def __init__(self):
        self.__Primero = None
        self.__Ultimo = None

    def Obtener_Vacio(self):
        if self.__Primero ==None:
            return True    

    def Insertar_al_Inicio(self, elemento):
        if self.Obtener_Vacio()==True:
            self.__Primero = elemento
            self.__Ultimo = elemento
        else:
            elemento.pSig = self.__Primero
            self.__Primero = elemento 

    def Insertar_al_Final(self, elemento):
        if self.Obtener_Vacio()==True:
            self.__Primero = elemento 
            self.__Ultimo = elemento
        else:
            elemento.pSig = self.__Ultimo
            self.__Ultimo = elemento            

    def Eliminar_al_Inicio(self):
        if self.Obtener_Vacio()==True:
            print ("No se puede eliminar, la lista se encuentra vacia")
        elif self.__Primero == self.__Ultimo:
            self.__Primero = None
            self.__Ultimo = None
            print("Elemento eliminado, la lista ahora se encuentra vacia")
        else:
            #temp = self.__Primero
            self.__Primero = self.__Primero.pSig
            #temp = None
            print ("Elemento eliminado")

    def Eliminar_al_Final(self):  
        if self.Obtener_Vacio()==True:
            print("No se peude eliminar, la lista se encuentra vacia")
        elif self.__Primero == self.__Ultimo:
            self.__Primero = None
            self.__Ultimo = None
            print("Elemento eliminado, la lista ahora se encuentra vacia")
        else:
            validar = True
            temp = self.__Primero
            while(validar):
                if temp.pSig == self.__Ultimo:
                    #temp2 = self.__Ultimo
                    self.__Ultimo = temp
                    #temp2 = None
                    validar = False
                    print("Elemento eliminado")
                else:
                    temp = temp.pSig    

    def primeroAUltimo(self):
        if self.Obtener_Vacio() == True:
            return ("La lista se encuentra vacia")
        else:
            return self.__Primero

    def UltimoaPrimero(self):
        if self.Obtener_Vacio() == True:
            return ("La lista se encuentra vacia")
        else:
            return self.__Ultimo    

    def Imprimir_PrimeroUltimo(self):
        if self.Obtener_Vacio()==True:
            print("La lista se encuentra vacia")
        else:
            validar = True
            temp = self.__Primero
            while(validar):
                print(temp.Obtener_Elemento())
                if temp == self.__Ultimo:
                    validar=False
                else:
                    temp = temp.pSig

    def modificar(self, elemento, elementoModificar):
        aux = self.__Primero
        anterior = aux
        while aux != None:
            if str(aux) == str(elemento):
                print("Dato Encontrado y Modificado")
                elementoModificar.pSig = aux.pSig
                anterior.pSig = elementoModificar
                return True
            anterior = aux
            aux = aux.pSig     

if __name__ == "__main__":
    correcto = False
    num=0
    ls = Lista()   
    salir = False
    opcion = 0

    while (not salir):
        print ("1. Insertar al Inicio ")
        print ("2. Insertar al final")
        print ("3. Modificar")
        print ("4. Imprimir de ultimo a primero")
        print ("5. Eliminar al Inicio")
        print ("6. Eliminar al final")
        print ("7. Salir")

        num = int(input("Escoja una opcion: ")) 

        opcion = num

        if opcion == 1:
            print("Estoy en la opcion Insertar al Inicio")
            dat = input("Ingrese un dato: ")
            nod= Nodo(dat)
            ls.Insertar_al_Inicio(nod)
        elif opcion == 2:
            print("Estoy en la opcion Insertar al final")
            dat = input("Ingrese un dato: ")
            nod= Nodo(dat)
            ls.Insertar_al_Final(nod)
        elif opcion == 3:
            print("Estoy en la opcion modificar")
            dat = input("Ingrese un dato a buscar: ")
            datM = input("Ingrese dato a modificar: ")
            nodE= Nodo(dat)
            nodEM =Nodo(datM)
            ls.modificar(nodE, nodEM)
        elif opcion == 4:
            print("Estoy en la opcion Imprimir de primero a ultimo")
            ls.Imprimir_PrimeroUltimo()
        elif opcion == 5:
            print("Estoy en la opcion eliminar al inicio")
            ls.Eliminar_al_Inicio()
        elif opcion == 6:
            print("Estoy en la opcion eliminar al final")
            ls.Eliminar_al_Final()
        elif opcion == 7:
            print("Nos vemos O/") 
            salir = True
        else:
            print("Ingrese una opcion valida")

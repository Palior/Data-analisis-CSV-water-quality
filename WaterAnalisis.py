# -*- coding: cp1252 -*-
#Programa que realiza el analisis de calidad del agua, por regiones a partir de un archivo csv que contiene
#datos de muestras de pozos, para finalmente entregar graficos con respecto al agua potable y no potable
#Autor: Pablo Lizama
#Python 3.7.1

#BLOQUE DE DEFINICION

#DEFINICION DE CONSTANTES

#IMPORTACION DE FUNCIONES

#DEFINICION DE FUNCIONES
#Funcion que realiza la lectura del archivo formato csv
#Entrada: ubicacion del archivo a leer
#Salida: Archivo leido, como lista de strings que incluyen el caracter especial "\t"
def leerArchivo(ubicacion):
    archivo=open(ubicacion,"r") #se abre el archivo y se guarda internamente
    textoLeido=archivo.read().splitlines() #se realiza la lectura del archivo, a la vez que se separa en distintos string, diferenciados por filas del archivo
    archivo.close #se cierra el archivo abierto, ya que no se utilizara denuevo y solo utiliza memoria
    return textoLeido


#Funcion que ordena la lista de listas por region, dejando juntas las que son la misma
#Entrada: Lista de Listas con strings en su interior que contienen informacion
#Salida: Lista de Listas agrupadas por region
def ordenarPorPozo(listaDeListas):
    pozos=[] #lista vacia para guardas los pozos que ya fueron ordenados
    listaOrdenada=[] #lista vacia que contendra la lista de listas ordenada por pozo
    contador=0 #contador de la posicion en la que se encuentra el primer elemento a comparar
    for lista in listaDeListas: #ciclo para recorrer la lista
        if not lista[1] in pozos: #determina si la region presente en la lista actual, esta o no en la variable regiones
            listaOrdenada.append(lista) #se agrega a la lista ordenada
            posicion=contador+1 #posicion del elemento con el que se compara el pozo
            while posicion<len(listaDeListas):#ciclo para comparar una sublista con las siguientes
                if lista[1]==listaDeListas[posicion][1]: #comparacion del elemento con el que esta en la variable posicion
                    listaOrdenada.append(listaDeListas[posicion]) #si su primer elemento que es el pozo es igual, entonces se agrega a la lista ordenada
                posicion=posicion+1 #se aumenta la posicion para avanzar en el ciclo
            pozos.append(lista[1])
        contador=contador+1 #aumenta la cuenta de la posicion del elemento lista del ciclo
    return listaOrdenada
        
def ordenarPorRegion(listaOrdenada):
    regiones=[] #lista vac�a para guardar las regiones que ya #fueron ordenadas
    listaOrdenada2=[] #lista vac�a que contendr� la lista de listas #ordenada por regi�n
    contador=0 #contador de la posici�n en la que se encuentra el #primer elemento a comparar
    for lista in listaOrdenada: #ciclo para recorrer la lista
        if not lista[0] in regiones: #determina si la regi�n #presente en la lista actual, est� o no en la variable regiones
            listaOrdenada2.append(lista) #se agrega a la lista #ordenada
            posicion=contador+1 #posicion del elemento con el que #se compara la region
            while posicion<len(listaOrdenada):#ciclo para comparar #una sublista con las siguientes
                if lista[0]==listaOrdenada[posicion][0]: #comparaci�n del elemento con el que est� en la variable posicion
                    listaOrdenada2.append(listaOrdenada[posicion]) #si su primer elemento, que es la region, es igual, entonces se #agrega a la lista ordenada
                    #print (listaOrdenada2)
                posicion=posicion+1 #se aumenta la posicion para #avanzar en el ciclo
            regiones.append(lista[0])
        contador=contador+1 #aumenta la cuenta de la posicion del #elemento lista del ciclo
    return listaOrdenada2

#lista Ordenada 2 es la que nos sirve ya que esta ordenada por region ya



def cantidadmuestras(listaOrdenada2):       #Calcular la cantidad de muestras en cada pozo
    contador=0                             #contador para la cantidad de veces que aparece un pozo
    listapozos=[]                          #lista con los pozos para contarlos
    listaMuestras=[]                       #Lista con las muestras contadas 
    agregados=[]                           #para preguntar si ya lo agrego
    for muestra in listaOrdenada2:          #Extrae cada pozo y lo agrega a una nueva lista
        listapozos.append(muestra[1])
        #ListaPozos estara de la forma ["M1","M1","M1","M2","M2","V1"...etc] 
    
    for  pozo in listapozos :              #recorre la lista con pozos pd : cada pozo esta en string  
        #Agrega una lista de par ordenado, la muestra con el nombre del pozo y la cantidada de veces que aparece
        #que determina cuantas muestras tendra
        
        contador=int(listapozos.count(pozo))
        if pozo not in agregados :         # con esto pregunta si ya fue agregado tal pozo con sus muestras
            listaMuestras.append([pozo,contador])
        agregados.append(pozo)                                     

    return listaMuestras                         
# aqui se espera que este de esta manera, listaMuestras=[[pozo1,50],[pozo2,35]] donde el numero siguiente es la cantidad de muestras
#el primero en string y el segundo en numero


#listaMuestras=cantidadmuestras(ListaOrdenada2)

#print(listaMuestras)


def analizarTurbiedad(listaOrdenada2,listaMuestras): 
    #comenzamos con la condicion mas global, ninguna muestra > 20 NTU
    pozosSiA=[]
    pozosNoA=[]
    #retornar pozosTotal con ambas listas
    pozosTotalA=[]
    
    for muestra in listaOrdenada2 :           #analiza la turbiedad de cada muestra y rescata su pozo si cumple
        if float(muestra[3]) > 20 :   #NTU        
            pozosNoA.append(muestra[1])    #Correspondiente al pozo
            
        else:
            pozosSiA.append(muestra[1])
            
    #como guardara mas de una vez el pozo, ej : ["M1","M1"..etc]
    #en ambas listas  se eliminara hasta n-1 veces        
    
    for pozo in pozosSiA:
        contador1=pozosSiA.count(pozo)
        if contador1!=1:         #es decir que habra mas de uno
            pozosSiA.remove(pozo)
            
    for pozo in pozosNoA:
        contador2=pozosNoA.count(pozo)
        if contador2!=1:
            pozosNoA.remove(pozo)

    #Ya en este punto deberia estar como ["M1","M2","M3"..etc] cada lista
    #ver si no hay elementos en pozosno que se repitan en pozosSi que son candidatos

    for pozo in pozosNoA:
        if pozo in pozosSiA:
            pozosSiA.remove(pozo)
    
            
    #De esta forma me quedan en pozosposibles los que sirven realmente
    #Ahora necesitamos analizar la condicion   4 NTU < 5 % de muestras
    #quiere decir que el 5 % de muestras en mi pozo pueden superar 4 NTU manteniendose potable el pozo
    #ocupando la informacion de la funcion cantidad de muestras donde retorna
            
    #listaMuestras=[[pozo1,10],[pozo2,50]] , analizando solo en los pozossi
    #el primero en string y el segundo en numero
            
   
    #pozo es cada par ordenado
    
    for pozo in listaMuestras:
        # hay que ver si toma la informacion entregada por la otra funcion,
        #Quiza guardarla en un a variable para llamarla luego
        contador4=0
        
        if pozo[0] in pozosSiA:
            
            #solo necesito rescatar su numero para ver cuantas muestras pueden cumplir el factor limitante
            #solo si se encuentra en pozossi
            contador3=int(pozo[1]*(5/100)+1)
            
 
            
            listaMuestras#con esto me aseguro que 0.9 muestras pasen a 1 y 5.5 muestras pasen a 6
            
            for muestra in listaOrdenada2:   
                if pozo[0]==muestra[1]:
                    
                    #con esto analizo solo los pozos restantes que son candidatos bajo pozosSi y
                    #que sean el mismo en la lista ordenada, es decir al pozo correcto
                    if muestra[3] > 4 : #NTU
                        
                        contador4=contador4+1
                        
                    if contador4 > contador3 and pozo[0] in pozosSiA:
                        pozosSiA.remove(pozo[0])
                        pozosNoA.append(pozo[0])
                            
                  

    #Con esto si contador 4 supera a condador 3 quiere decir que hay mas de un 5%
    #de muestras que superan el limite , por lo cual el pozo pasa a ser No potable
    #removiendolo de pozossiA con la condicion de eliminar siempre que haya uno que elimnar
    #Y agregandolo a la lista de los no potables directamente                    
    #Ahora si filtramos completamente ambas listas                 
            
    pozosTotalA.append(pozosSiA)  #agregamos listas a otra lista
    pozosTotalA.append(pozosNoA)

    return pozosTotalA

#Primera lista importante

#ListaTurbiedad=analizarTurbiedad(ListaOrdenada2,listaMuestras)

#Donde la primera lista de listas son los pozos que pasaron completamente el primer control
#y la segunda los que no


#Segundo control

def analizarDesinfeccion(listaOrdenada2,listaMuestras):
    #comenzamos con condicion mas global, concentracion maxima de cada muestra
    #2mg/l
    pozosNoB=[]
    pozosTotalB=[]
    pozosSiB=[]
    #retornar pozosTotal con ambas listas
    for muestra in listaOrdenada2:
        #analiza la desinfeccion de cada muestra y rescata su pozo si cumple
        #2mg/l
        if muestra[4] > 2:
            pozosNoB.append(muestra[1])   
        else:
            pozosSiB.append(muestra[1])
           
           
    #como guardara mas de una vez el pozo, ej : ["M1","M1"..etc]
    #en ambas listas  se eliminara hasta n-1 veces
                     
    for pozo in pozosSiB :
        contador1=pozosSiB.count(pozo)
        if contador1!=1:         
            pozosSiB.remove(pozo)
           
    for pozo in pozosNoB:
        contador2=pozosNoB.count(pozo)
        if contador2!=1:
            pozosNoB.remove(pozo)
    #Ya en este punto deberia estar como ["M1","M2","M3"..etc] cada lista
    #ver si no hay elementos en pozosno que se repitan en pozosSi que son candidatos

    for pozo in pozosNoB:
        if pozo in pozosSiB:
            pozosSiB.remove(pozo)
            
    #De esta forma me quedan en pozos posibles los que sirven realmente
    #Ahora necesitamos analizar la condicion   0,2mg/l < 10 % de muestras
    #ocupando la informacion de la funcion cantidad de muestras donde retorna
            
    #listaMuestras=[[pozo1,10],[pozo2,50]] , analizando solo en los pozos si        

    for pozo in listaMuestras:
        # hay que ver si toma la informacion entregada por la otra funcion,
        #Quiza guardarla en un a variable para llamarla luego
        contador4=0
        if pozo[0] in pozosSiB:
            #solo necesito rescatar su numero para ver cuantas muestras pueden cumplir el factor limitante
            #solo si se encuentra en pozossi
            contador3=int(pozo[1]*(1/10)+1)
            #con esto me aseguro que 0.9 muestras pasen a 1 y 5.5 muestras pasen a 6
          
            for muestra in listaOrdenada2:
                if pozo[0]==muestra[1]:
                    if  muestra[4] > 0.2 : #mg/l
                        contador4=contador4+1
                     
                    if contador4 > contador3 and pozo[0] in pozosSiB:
                        pozosSiB.remove(pozo[0])
                        pozosNoB.append(pozo[0])                  
                            
                        
    #Con esto si contador 4 supera a condador 3 quiere decir que hay mas de un 10%
    #de muestras que superan el limite , por lo cual el pozo pasa a ser No potable
    #removiendolo de pozossiB con la condicion de elimnar siempre que haya uno que elimnar
    #Ahora si filtramos completamente ambas listas                    

    pozosTotalB.append(pozosSiB)
    pozosTotalB.append(pozosNoB)

    return pozosTotalB
                            
#Segunda lista importante

#ListaDesinfeccion=analizarDesinfeccion(ListaOrdenada2,listaMuestras)


#Tercer control

def analizarMicrobiologico(listaOrdenada2,listaMuestras):
    pozosSiC=[]
    pozosNoC=[]
    pozosTotalC=[]
    #aqui el problema es que hay dos condiciones con porcentajes  5% y 10%
    #primero hay que identificar cuantas muestras habran
    
    #listaMuestras=[[pozo1,10],[pozo2,50]], tomando todos los pozos,
    #sin saber si son potables o no

    #trabajar con los parametros  1col/100ml<10% y 5col/100ml < 5% muestras

    chequeados=[]   #revisar si ya fue analizado el pozo
    for pozo in listaMuestras:
        #no se necesita ver si hay algun pozo posible para igualar
        contador1=int(pozo[1]*(1/10)+1)
        contador2=int(pozo[1]*(5/100)+1)
        contador11=0
        contador22=0
        
        if pozo[0] not in chequeados:
            
            for Muestra in listaOrdenada2:
                # Revisar
                if pozo[0]== Muestra[2]:
                    
                    if Muestra[2] > 1 : #Col/100ml
                        contador11= contador11 +1
                    if Muestra[2] > 5 :
                        contador22= contador22 +1
                    
                
        chequeados.append(pozo[0])        
        
        #Antes solo debia eliminar los que no me siven, ahora debo agregar los
        #que cumplan con ambas a la vez lo que quiere decir que los pozos que me
        #serviran seran los contadores 11 y 22 no superen a la vez al 1 y 2,
        #pero para ello deben finalizar su for para saber el total        

        if contador11 < contador1  and   contador22 < contador2 :
            pozosSiC.append(pozo[0])
        else:
            pozosNoC.append(pozo[0])

    pozosTotalC.append(pozosSiC)
    pozosTotalC.append(pozosNoC)

    return pozosTotalC

#Tercera lista Importante

#ListaMircrobiologico=analizarMicrobiologico(ListaOrdenada2,listaMuestras)


#Lista final


def listaDefinitiva(listaTurbiedad,listaDesinfeccion,listaMircrobiologico):
    potable=[]
    noPotable=[]
    final=[]
    #Contadores i,j,k para cada parametro
    #agregando a potable la primera lista
    #de lista y a no potable la segunda lista de lista
    i=0
    for listas in listaTurbiedad:    #accede a ambas listas , con el control pasado y las no potables
        
        for pozo in listas:          #accede primero a los datos posibles
            if i==0:
                potable.append(pozo)
            else:
                noPotable.append(pozo)
                
        i=i+1

    # Y asi con las siguientes
    j=0
    for listas in listaDesinfeccion:    #accede a ambas listas , con el control pasado y las no potables
        
        for pozo in listas:          #accede primero a los datos posibles
            if j==0:
                potable.append(pozo)
            else:
                noPotable.append(pozo)
                
        j=i+1

    k=0
    print(potable)
    for listas in listaMircrobiologico:    #accede a ambas listas , con el control pasado y las no potables
        
        for pozo in listas:          #accede primero a los datos posibles
            if k==0:
                potable.append(pozo)
            else:
                noPotable.append(pozo)
                
        k=i+1

    #Ahora tenemos una lista con potables y otra no potable, pero puede ser
    #con elementos repetidos

    editado=potable
    for pozo in potable:
        contador2=editado.count(pozo)
        if contador2!=1:
            editado.remove(pozo)
            
    editado2=noPotable        
    for pozo in noPotable:
        contador2=editado2.count(pozo)
        if contador2!=1:
            editado2.remove(pozo)

    #ya eliminado los duplicados ver si no hay elementos en noPotables
    #que se repitan en potables

    for pozo in editado2:
        if pozo in editado:
            editado.remove(pozo)
            
    #finalizando ya tendriamos todo filtrado
            
    final.append(editado)
    final.append(editado2)
    return final


#retornando ahora si una lista de listasmencionando los pozos
#con la primera potable y la segunda no potable

#final= ListaDefinitiva(ListaTurbiedad,ListaDesinfeccion,ListaMircrobiologico)
#print (final)





            
#BLOQUE PRINCIPAL

#ENTRADA
ubicacion=input("ingrese la ubicacion del archivo formato csv de la forma disco:/carpeta1/carpeta2/nombreDelArchivo ")

#PROCESO
        
textoLeido=leerArchivo(ubicacion)
lista=[]
for elemento in textoLeido: #ciclo que recorre elementos del texto leido
    if ";" in elemento:
        separado=elemento.split(";")#se separan los string contenidos en la lista a partir de los caracteres";"
    elif "," in elemento:
        separado=elemento.split(",")#se separan los string contenidos en la lista a partir de los caracteres","
    lista.append(separado) #se agrega la lista generada anteriormente a una lista
lista.pop(0) #se elimina la primera fila que contielistaMuestrasne solo los titulos
listaDeListas=lista #se guarda lo anteriormente mencionado en una variable mas comoda


listaOrdenada=ordenarPorPozo(listaDeListas)
listaOrdenada2=ordenarPorRegion(listaOrdenada)

i=0
for lista in listaOrdenada2:
    listaOrdenada2[i][2]=float(lista[2])
    listaOrdenada2[i][3]=float(lista[3])
    listaOrdenada2[i][4]=float(lista[4])
    i=i+1

listaMuestras=cantidadmuestras(listaOrdenada2)
listaTurbiedad=analizarTurbiedad(listaOrdenada2,listaMuestras)
listaDesinfeccion=analizarDesinfeccion(listaOrdenada2,listaMuestras)
listaMircrobiologico=analizarMicrobiologico(listaOrdenada2,listaMuestras)
final= listaDefinitiva(listaTurbiedad,listaDesinfeccion,listaMircrobiologico)


potables=final[0]
noPotables=final[1]

print("Los pozos potables son", potables)
print("Los pozos no potables son", noPotables)



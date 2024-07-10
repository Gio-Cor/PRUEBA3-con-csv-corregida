
import csv

'''La empresa de eSports “eShirlitos”, necesita desarrollar un sistema que permita registrar los puntajes obtenidos por sus competidores en Fortnite, Valorant y Fifa. Para el funcionamiento del sistema se requiere las siguientes funcionalidades
1.
Registrar puntajes torneo
2.
Listar los todos puntajes
3.
Imprimir por Tipo 
4.
Salir del programa'''
listadepuntaje={}
listadepuntos=[]
EXPERTO=[]
AVANZADO=[]
PRINCIPIANTE=[]
def registro():


    while True:
        try:
            idjugador=input('Ingresa tu ID de jugador')
            if len(idjugador)!=0:            
                listadepuntaje['Id Jugador']=idjugador 
                break
            else:
                print('Debe tener al menos un caracter')
        except: 
            print('No numeros')

    while True:
        try:
            nombre=input('Ingresa tu Nombre y apellido')
            if len(nombre)!=0:            
                listadepuntaje['Nombre']=nombre 
                break
            else:
                print('Ingresa al menos un caracter')
        except: 
            print('Error')


    while True:
        try:
            juego=input('Ingresa el juego').upper()
            if len(juego)!=0:            
                if juego=='VALORANT' or juego=='FORNITE' or juego=='FIFA': 
                    if juego=='VALORANT':
                        puntaje=int(input('Escribe tu puntaje'))
                        listadepuntaje['VALORANT']=puntaje
                        break
                        

                    if juego=='FORNITE':
                        puntaje=int(input('Escribe tu puntaje'))
                        listadepuntaje['VALORANT']=puntaje
                        break
                        

                    if juego=='FIFA': 
                        puntaje=int(input('Escribe tu puntaje'))  
                        listadepuntaje['VALORANT']=puntaje
                        break
                else:
                    print('Fuera de rango')
            else:
                print('Recuerda elegir un juego')
        except: 
            print('Ingrese al menos un caracter')
    #Elecció del juego
    
    while True:
        listadepuntos.append(listadepuntaje)
        try:
            eleccion=int(input('''1.-Principiante - 2.-Avanzado - 3-Experto
        >'''))
            if eleccion==1 or eleccion==2 or eleccion==3:
                if eleccion==1:
                    PRINCIPIANTE.append(listadepuntos)
                    break
                if eleccion==2:
                    AVANZADO.append(listadepuntos)
                    break
                if eleccion==3:
                    EXPERTO.append(listadepuntos)  
                    break 
            else:
                print('Opción no encontrada')
        except: 
            print('ERROR')

   
'''Listar puntajes

Debe mostrar en la pantalla la lista de todos los puntajes registrados, similar al ejemplo anterior (opción 1).'''

def listadepuntajes():
    if len(listadepuntos)>=1:
        print(listadepuntos)
    else:
        print('No hay registros')


'''Para imprimir por tipo, el usuario debe seleccionar alguno de los 3 tipos (Principiante - Avanzado - Experto). 
Estos tipos deben estar previamente definidos en algún tipo de colección de Python en el código.
Al seleccionar uno de los tipos, se generará un archivo de texto (.txt) con el detalle de los puntajes obtenidos 
por los jugadores del tipo seleccionado. Este debe tener la misma forma del registro completo de las opciones anteriores, 
pero en archivo de texto.
Cada opción de la aplicación debe desarrollarse en una función que debe llamarse desde el programa principal.'''

def imprimirportipo():
    eleccion=''
    print('Seleccione una de las opciones siguientes')
    print(PRINCIPIANTE)
    print(AVANZADO)
    print(EXPERTO)
    eleccion=int(input('''1.-Principiante - 2.-Avanzado - 3-Experto
    >'''))
    if eleccion==1 or eleccion==2 or eleccion==3:
        if eleccion==1:
            with open('Puntaje-Principiante.csv','w',newline='') as archivo:
                escribir=csv.writer(archivo)     
                escribir.writerow(PRINCIPIANTE) 
        if eleccion==2:
            with open('Puntaje-avanzado.csv','w',newline='') as archivo:
                escribir=csv.writer(archivo)     
                escribir.writerow(AVANZADO) 
        if eleccion==3:
            with open('Puntaje-experto.csv','w',newline='') as archivo:
                escribir=csv.writer(archivo)
                escribir.writerow(EXPERTO) 

    else:
        print('Opción no existe')
    





def menu():
    op=0
    while True:
        print('''
1.-Registrar puntajes torneo
2.-Listar los todos puntajes
3.-Imprimir por Tipo
4.-Salir del programa''')
        try:
            op=int(input(''''Elige tu opción
            >'''))
            if op>=1 and op<=4:
                if op==1:
                    registro()
                if op==2:
                    listadepuntajes()
                if op==3:
                    imprimirportipo()
                if op==4:
                    print('Hasta pronto')
                    break
            else:
                print('Opción fuera de rango')

        except:
            print('Opción debe ser un numero ')
            

menu()
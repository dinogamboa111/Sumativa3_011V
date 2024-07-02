import csv
from random import *
import os
import time
txtbmientras=""
txtctmientras=""
txtsbmientras=""

Nropedinicial=randint(1,1000)
Nroped = 0
Nroped = Nropedinicial
condicion = True
limpiarpantalla="cls"
Resgistropedido =[["Nro.Ped", "Cliente", "Direcció", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"]]
dato1= "Nro.Ped, Cliente, Direcció, Sector, Saco 5kg, Saco 10kg, Saco 20kg"
txtsb=f"{dato1}"
txtb =f"{dato1}"
txtct=f"{dato1}"
txtbformat = txtb.format( txtb + txtbmientras) 
txtctformat = txtct.format( txtct + txtctmientras)
txtsbformat = txtsb.format( txtsb + txtsbmientras)
    
os.system(limpiarpantalla)
def registrarpedido():
    
    eliminar = 0
    eliminar += 1
    cliente= input("Favor indique su nombre: ")
    Direccion= input("Favor indique su direccion: ")
    Sector= input("Favor indiquenos su comuna(San bernardo, Calera de tango o buin): ")
    Sectormod = Sector.lower 
    saco5kg=0
    saco10kg=0
    saco20kg=0
    while True:
        try:
            tiposaco=int(input("""Indique que tipo de saco desea comprar:
                        1-Saco 5 kg
                        2-Saco 10kg
                        3-Saco 20kg
                        4-Terminar eleccion de sacos.
                        """))
            if tiposaco == 1:
                saco5kg=int(input("Indique cuantos sacos de 5kg desea: "))
            elif tiposaco == 2:
                saco10kg=int(input("Indique cuantos sacos de 10kg desea: "))
            elif tiposaco == 3:
                saco20kg=int(input("Indique cuantos sacos de 20kg desea: "))
            elif tiposaco == 4:
                break
                
        except ValueError:
            print("Debe ingresar una eleccion numerica. ")
            continue
    Resgistropedido.append([Nroped, cliente, Direccion, Sector, saco5kg, saco10kg, saco20kg])
    if Sector == "" or cliente == "" or Direccion == "":
        print("Falto un dato, favor vuelta a registrar")
        Resgistropedido.remove(Resgistropedido[eliminar])
    elif Sectormod == "san bernardo":
        txtsbmientras = f"{Nroped},{cliente},{Direccion},{Sector},{saco5kg},{saco10kg},{saco20kg}"
       
    elif Sectormod == "calera de tango":
        txtctmientras= f"{Nroped},{cliente},{Direccion},{Sector},{saco5kg},{saco10kg},{saco20kg}"
        
    elif Sectormod == "buin":
        txtbmientras= f"{Nroped},{cliente},{Direccion},{Sector},{saco5kg},{saco10kg},{saco20kg}"
        
    else:
        print("Comuna mal ingresada, favor vuelta a registrar.") 

def listarpedidos():
    for fila in Resgistropedido:
        print(fila)

def hojaderuta():
    
    txtsb=f"""{dato1}"""
    sectorhojaruta= int(input("""Hojas de ruta :
                             1-Hoja de ruta San Bernardo
                             2-Hoja de ruta Calera de Tango
                             3-Hoja de ruta de buin
                             indique su eleccion: """))
    if sectorhojaruta == 1:
        
        with open ('hojasanbernardo.txt','w',newline='') as hojasb_txt:
            hojasb_txt.write(txtsbformat)
        with open ('hojasanbernardo.txt','r',newline='') as hojasb_txt:
            hojasb_txt.read()
            print(txtsbformat)

def guardadocsv():
    nombrearchivo = input(f"Ha salido, su comprar sera guardada, indique nombre del archivo.\nejemplo: 'Aquisunombre.csv' ")
    with open(nombrearchivo, 'w',newline='') as Archivo_csv:
        Escritor_csv=csv.writer(Archivo_csv)
        Escritor_csv.writerows(Resgistropedido)


while condicion:

    try:
        menu = int(input("""Bienvenidos a CatPremium, 
            1-Registrar pedido
            2-Listar los todos los pedidos
            3-Imprimir hoja de ruta
            4-Salir del programa
                favor indicar su elección: 
    """))
        if menu == 1:
            registrarpedido()
            Nroped += 1  
        elif menu == 2:
            listarpedidos()
        elif menu == 3:
            hojaderuta()
        elif menu == 4:
            guardadocsv()
            break
       
    except ValueError:
        print("Debe ingresar opcion entre 1 y 4.")
        continue




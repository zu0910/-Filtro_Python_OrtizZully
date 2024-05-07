import json

with open ("prueba.json",encoding="utf-8") as file:
    archivo=json.load(file)
#crear usuARIO, VER CLIENE, actualizar, eliminar salir
bol1=True
while bol1==True:
    print("----------MENU PRINCIPAL-------------\n 1).Administrador\n 2). Salir\n")
    opc=int(input("Ingrese una opcion del menu anterior:\n"))

    if opc==1:
        bol2=True
        while bol2==True:

            print("------------Menu Administrador-----------\n 1).Crear usuario\n 2).Ver usuarios\n 3). Actualizar usuario\n 4). Eliminar usuario\n 5). Salir")
            opcMenuAdm=int(input("Ingrese una de las opcioens del menu anterior:\n"))
            

            if opcMenuAdm==1:
                #Crear usuario
                print("Crear usuario:\n")
                for i in range(0,len(archivo)):

                    NewName=input("Ingrese el nombre del nuevo usuario:\n")
                    archivo["newUsu"][i]["Nombre"][0]=NewName
                    NewDireccion=input("Ingrese la direccion:\n")
                    archivo["newUsu"][i]["Direccion"][0]=NewDireccion
                    NewConta=int(input("Ingrese el contacto\n"))
                    archivo["newUsu"][i]["Contacto"][0]=NewConta

            elif opcMenuAdm==2:
                #Ver usuarios
                print("Ver usuarios:\n")
                print("Nombre:", archivo["newUsu"][i]["Nombre"][0])
                print("Direccion:",archivo["newUsu"][i]["Direccion"][0])
                print("Contacto:",archivo["newUsu"][i]["Contacto"][0])

            elif opcMenuAdm==3:
                #Actualizar usuarios
                print("Actualizar usuarios")
                

            elif opcMenuAdm==4:
                #Eliminar usuarios
                print("Eliminar usuario")

            elif opcMenuAdm==5:
                bol2=False

    elif opc==2:
        bol1=False


 
            




    elif opc==2:
        bol1=False




vOp=0
sw=0
vCantidad=0
EntradaNiño=0
AcumEntradaNiño=0

EntradaJoven=0
AcumEntradaJoven=0

EntradaAdulto=0
AcumEntradaAdulto=0

total=AcumEntradaNiño+AcumEntradaJoven+AcumEntradaAdulto

while sw==0:
    print("-------BIENVIDO A CINE EL MORO-------")
    print("-----------------------------------------")
    print("1.- ENTRADA NIÑO [$5500]")
    print("2.- ENTRADA JOVEN [$7000]")
    print("3.- ENTRADA ADULTO [$9000]")
    print("4.- BOLETA")
    print("5.- SALIR")
    print("-----------------------------------------")
    vOp=int(input("ingrese una opcion: "))

    try:
        if vOp==1:
            EntradaNiño=int(input("ingrese la cantidad de entradas que desea: "))
            EntradaNiño+=vCantidad
            AcumEntradaNiño=EntradaNiño*5000
            print("usted desea", EntradaNiño, "entradas de niño")
        if vOp==2:
            EntradaJoven=int(input("ingrese la cantidad de entradas que desea: "))
            EntradaJoven+=vCantidad
            AcumEntradaJoven=EntradaJoven*7000
            print("usted desea", EntradaJoven, "entradas de joven")
        if vOp==3:
            EntradaAdulto=int(input("ingrese la cantidad de entradas que desea: "))
            EntradaAdulto+=vCantidad
            AcumEntradaAdulto=EntradaAdulto*9000
            print("usted desea", EntradaAdulto, "entradas de adulto")
        if vOp==4:
            print("-------BOLETA-------")
            print("==============================================================================================================")
            print("ARTICULO         CANTIDAD                    VALOR UNIDAD                          SUB-TOTAL")
            print("POLERAS",    EntradaNiño,                    "5000",                         AcumEntradaNiño) 
            print("CAMISAS",    EntradaJoven,                    "7000",                         AcumEntradaJoven) 
            print("PANTALON",   EntradaAdulto,                 "9000",                         AcumEntradaAdulto)
            print("==============================================================================================================")
            print("TOTAL A PAGAR: ",                                                               AcumEntradaNiño+AcumEntradaJoven+AcumEntradaAdulto)
        if vOp==5:
            print("PROGRAMA FINALIZADO")

    except:
        print("opcion invalida")
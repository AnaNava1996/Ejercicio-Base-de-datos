import copy

def borrarT(matriz):
    fila=int(input("escoja la fila: "))
    del(matriz[fila])

def borrarC(matriz):
    columna=int(input("escoja la columna:  "))
    for i in range(0,len(matriz)):
        del(matriz[i][columna-1])

def introducirdatos(matriz):
    fila=int(input("Fila: "))
    columna=int(input("Columna: "))
    op=input("\nElija 'i' para entero\nElija 's' para cadena o caracter:  ")
    if(op=='i'):
        dato=int(input("Dato: "))
    elif(op=='s'):
        dato=input("Dato: ")
    matriz[fila][columna]=dato
    return matriz

def mostrartabla(matriz):
    print("\n")
    for i in range(0,len(matriz)):
        print(matriz[i])
    print("\n")

def proyeccion(matriz):
    matrizaux=[[None] * 0 for i in range(0)]
    cad=str(input("columnas: "))
    for i in range(0,len(matriz)):
        matri=[]
        for k in cad:
            matri.append(matriz[i][int(k)-1])
        matrizaux.append(matri)
    op=int(input("Seleccion...1.Si, 2.No:  "))
    if(op==1):
        seleccion(matrizaux)
    else:
        opc=int(input("Cruz...1.Si,2.No:  "))
        if(opc==1):
            cruz(matrizaux,matriz1,matriz2,matriz3)
        else:
            mostrartabla(matrizaux)

def seleccion(matriz):
    matrizaux=[[None] * 0 for i in range(0)]
    atributo=input("Atributo: ")            
    condicion=int(input("1.MAYOR\n2.MENOR\n3.IGUAL\n"))
    op=input("Elija 'i' para entero\nElija 's' para cadena o caracter:  ")
    if(op=='i'):
        valor=int(input("Valor: "))
    elif(op=='s'):
        valor=input("Valor: ")
    matrizaux.append(matriz[0])
    while(condicion!=0):
        if(condicion==1):
            for j in range(0,len(matriz[0])):
                if(atributo==matriz[0][j]):
                    for i in range(0,len(matriz)):
                        if(type(matriz[i][j]) is int):                            
                            if(matriz[i][j]>valor):
                                matrizaux.append(matriz[i])
                        else:
                            pass
                    condicion=0
        elif(condicion==2):
            for j in range(0,len(matriz[0])):
                if(atributo==matriz[0][j]):
                    for i in range(0,len(matriz)):
                        if(type(matriz[i][j]) is int):                            
                            if(matriz[i][j]<valor):
                                matrizaux.append(matriz[i])
                        else:
                            pass
                    condicion=0           
        elif(condicion==3):
            for j in range(0,len(matriz[0])):
                if(atributo==matriz[0][j]):
                    for i in range(0,len(matriz)):
                        if(matriz[i][j]==valor):
                                matrizaux.append(matriz[i])
                        else:
                            pass
                    condicion=0  
        elif(condicion==0):
            condicion=0
        else:
            condicion=0
            print("\nerror\n")
        op2=int(input("Proyeccion...1.Si, 2.No: "))
        if(op2==1):
            proyeccion(matrizaux)
        else:
            mostrartabla(matrizaux)

def agregarC(matriz):
    for i in range(0,len(matriz)):
        matriz[i].append(None)
    atributo=input("Nombre del atributo: ")
    b=len(matriz[0])
    matriz[0][b-1]=atributo
    mostrartabla(matriz)

def agregarT(matriz):
    for i in range(0,len(matriz)):#cantidad de filas...
        p=len(matriz[i])#cantidad de columnas.
    matriz.append([None]*p)
    mostrartabla(matriz)

def cruz(matrizaux,matriz1,matriz2,matriz3):
    op=6
    while(op!='0'):
        op=input("escoja la matriz a,b,c: ")
        if(op=='a'):
            if(matrizaux==[[None] * 0 for i in range(0)]):
                for i in range(0,len(matriz1)):
                    matrizaux.append(matriz1[i])
            else:
                a=len(matrizaux)-1
                b=len(matriz1)-1
                matrizaux2=[[None] * 0 for i in range((a*b)+1)]
                matrizaux2[0].extend(matrizaux[0])
                matrizaux2[0].extend(matriz1[0])
                k=0
                for i in range(1,len(matrizaux)):
                    for j in range(1,len(matriz1)):
                        k=k+1
                        matrizaux2[k].extend(matrizaux[i])
                        matrizaux2[k].extend(matriz1[j])
                mostrartabla(matrizaux2)
                matrizaux=matrizaux2
                opp=int(input("Proyeccion...1.Si, 2.No: "))
                if(opp==1):
                    proyeccion(matrizaux)
                else:
                    ops=int(input("Seleccion...1.Si, 2.No: "))
                    if(ops==1):
                        seleccion(matrizaux)
                    else:
                        mostrartabla(matrizaux)
        elif(op=='b'):
            if(matrizaux==[[None] * 0 for i in range(0)]):
                for i in range(0,len(matriz2)):
                    matrizaux.append(matriz2[i])
            else:
                a=len(matrizaux)-1
                b=len(matriz2)-1
                matrizaux2=[[None] * 0 for i in range((a*b)+1)]
                matrizaux2[0].extend(matrizaux[0])
                matrizaux2[0].extend(matriz2[0])
                k=0
                for i in range(1,len(matrizaux)):
                    for j in range(1,len(matriz2)):
                        k=k+1
                        matrizaux2[k].extend(matrizaux[i])
                        matrizaux2[k].extend(matriz2[j])
                mostrartabla(matrizaux2)
                matrizaux=matrizaux2
                opp=int(input("Proyeccion...1.Si, 2.No: "))
                if(opp==1):
                    proyeccion(matrizaux)
                else:
                    ops=int(input("Seleccion...1.Si, 2.No: "))
                    if(ops==1):
                        seleccion(matrizaux)
                    else:
                        mostrartabla(matrizaux)
        elif(op=='c'):
            if(matrizaux==[[None] * 0 for i in range(0)]):
                for i in range(0,len(matriz3)):
                    matrizaux.append(matriz3[i])
            else:
                a=len(matrizaux)-1
                b=len(matriz3)-1
                matrizaux2=[[None] * 0 for i in range((a*b)+1)]
                matrizaux2[0].extend(matrizaux[0])
                matrizaux2[0].extend(matriz3[0])
                k=0
                for i in range(1,len(matrizaux)):
                    for j in range(1,len(matriz3)):
                        k=k+1
                        matrizaux2[k].extend(matrizaux[i])
                        matrizaux2[k].extend(matriz3[j])
                mostrartabla(matrizaux2)
                matrizaux=matrizaux2
                opp=int(input("Proyeccion...1.Si, 2.No: "))
                if(opp==1):
                    proyeccion(matrizaux)
                else:
                    ops=int(input("Seleccion...1.Si, 2.No: "))
                    if(ops==1):
                        seleccion(matrizaux)
                    else:
                        mostrartabla(matrizaux)
        elif(op=='0'):
            op='0'
            break
    mostrartabla(matrizaux)

def Union(matrizaux,matriz1,matriz2,matriz3):
    da=[[None] * 0 for i in range(0)]
    ea=[[None] * 0 for i in range(0)]
    d=input("Seleccione tabla1, a,b,c: ")
    e=input("Seleccione tabla2, a,b,c: ")
    if(d=='a'):
        da=matriz1
    elif(d=='b'):
        da=matriz2
    else:
        da=matriz3
    if(e=='a'):
        ea=matriz1
    elif(e=='b'):
        ea=matriz2
    else:
        ea=matriz3    
    if(da[0]==ea[0]):
        matrizaux.append(da[0])
        for i in range(1,len(da)):
            matrizaux.append(da[i])
        for i in range(1,len(ea)):
            matrizaux.append(ea[i])
        mostrartabla(matrizaux)
    else:
        print("Incompatibles")

def Resta(matrizaux,matriz1,matriz2,matriz3):
    da=[[None] * 0 for i in range(0)]
    ea=[[None] * 0 for i in range(0)]
    aux=[[None] * 0 for i in range(0)]
    d=input("Seleccione tabla1, a,b,c: ")
    e=input("Seleccione tabla2, a,b,c: ")
    if(d=='a'):
        da=copy.copy(matriz1)
    elif(d=='b'):
        da=copy.copy(matriz2)
    else:
        da=copy.copy(matriz3)
    if(e=='a'):
        ea=matriz1
    elif(e=='b'):
        ea=matriz2
    else:
        ea=matriz3    
    if(da[0]==ea[0]):
        for i in range(1,len(da)):
            for j in range(1,len(ea)):
                if(ea[j]==da[i]):
                    aux.append(da[i])
        for i in range(0,len(aux)):
            da.remove(aux[i])
        mostrartabla(da)
    else:
        print("Incompatibles")

def Interseccion(matrizaux,matriz1,matriz2,matriz3):
    da=[[None] * 0 for i in range(0)]
    ea=[[None] * 0 for i in range(0)]
    d=input("Seleccione tabla1, a,b,c: ")
    e=input("Seleccione tabla2, a,b,c: ")
    if(d=='a'):
        da=copy.copy(matriz1)
    elif(d=='b'):
        da=copy.copy(matriz2)
    else:
        da=copy.copy(matriz3)
    if(e=='a'):
        ea=copy.copy(matriz1)
    elif(e=='b'):
        ea=copy.copy(matriz2)
    else:
        ea=copy.copy(matriz3)    
    if(da[0]==ea[0]):
        for i in range(0,len(da)):
            for j in range(0,len(ea)):
                if(da[i]==ea[j]):
                   matrizaux.append(da[i]) 
                else:
                    
                    pass
        mostrartabla(matrizaux)
    else:
        print("Incompatibles")





n1=int(input("Introduzca la cantidad de filas  de la matriz1 n: "))
m1=int(input("Introduzca el numero de columnas de la matriz1: "))
matriz1 =[[None] * m1 for i in range(n1)]
n2=int(input("Introduzca la cantidad de filas  de la matriz2 n: "))
m2=int(input("Introduzca el numero de columnas de la matriz2: "))
matriz2 = [[None] * m2 for i in range(n2)]
n3=int(input("Introduzca la cantidad de filas  de la matriz3 n: "))
m3=int(input("Introduzca el numero de columnas de la matriz3: "))
matriz3 = [[None] * m3 for i in range(n3)]
##########################################################################################

matriz1[0][0]="nombre"
matriz1[0][1]="edad"
matriz1[0][2]="tlf"
matriz1[1][0]="ana"
matriz1[1][1]=18
matriz1[1][2]="5555555"
matriz1[2][0]="pedro"
matriz1[2][1]=20
matriz1[2][2]="2222222"

matriz2[0][0]="nombre"
matriz2[0][1]="edad"
matriz2[0][2]="tlf"
matriz2[1][0]="laura"
matriz2[1][1]=22
matriz2[1][2]="5555555"
matriz2[2][0]="pablo"
matriz2[2][1]=21
matriz2[2][2]="2222222"
matriz2[3][0]="ana"
matriz2[3][1]=18
matriz2[3][2]="5555555"
matriz2[4][0]="pedro"
matriz2[4][1]=20
matriz2[4][2]="2222222"
'''
matriz3[0][0]="pa"
matriz3[0][1]="pe"
matriz3[0][2]="pi"
'''
menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
while(menu!=0):
    if(menu==1):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            introducirdatos(matriz1)
        elif(d=='b'):
            introducirdatos(matriz2)
        else:
            introducirdatos(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==2):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            agregarC(matriz1)
        elif(d=='b'):
            agregarC(matriz2)
        else:
            agregarC(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==3):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            agregarT(matriz1)
        elif(d=='b'):
            agregarT(matriz2)
        else:
            agregarT(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==4):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            mostrartabla(matriz1)
        elif(d=='b'):
            mostrartabla(matriz2)
        else:
            mostrartabla(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==5):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            proyeccion(matriz1)
        elif(d=='b'):
            proyeccion(matriz2)
        else:
            proyeccion(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==6):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            seleccion(matriz1)
        elif(d=='b'):
            seleccion(matriz2)
        else:
            seleccion(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==7):
        matrizaux=[[None] * 0 for i in range(0)]
        cruz(matrizaux,matriz1,matriz2,matriz3)
    elif(menu==8):
        matrizaux=[[None] * 0 for i in range(0)]
        Union(matrizaux,matriz1,matriz2,matriz3)        
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==9):
        matrizaux=[[None] * 0 for i in range(0)]
        Resta(matrizaux,matriz1,matriz2,matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==10):
        matrizaux=[[None] * 0 for i in range(0)]
        Interseccion(matrizaux,matriz1,matriz2,matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==11):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            borrarT(matriz1)
        elif(d=='b'):
            borrarT(matriz2)
        else:
            borrarT(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    elif(menu==12):
        d=input("escoja la matriz a,b,c: ")
        if(d=='a'):
            borrarC(matriz1)
        elif(d=='b'):
            borrarC(matriz2)
        else:
            borrarC(matriz3)
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    else:
        menu=int(input("\n1.Introducir o modificar dato.\n2.Agregar atributo.\n3.Agregar tupla.\n4.Mostrar tabla.\n5.Proyeccion.\n6.Seleccion.\n7.Producto cruz.\n8.Union.\n9.Resta.\n10.Interseccion.\n11.Borrar Tupla.\n12.Borrar Columna:  "))
    

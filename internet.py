# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Acceso a internet en Colombia
Modulo de funciones.

@author: Cupi2
"""
#llmas las librerias que necesitas.
import pandas as pd
import matplotlib.pyplot as plot

#Parte 1(listo)
#Cargar datos del archivo.csv
def cargar_datos(archivo:str)->pd.DataFrame:
    llamar=pd.read_csv(archivo,sep=",")
    return llamar
datos = cargar_datos("internet.csv")
#print(datos)

#Parte 2
#Requerimiento 1 (listo)
#Crear una grafica de torta de los departamentos y sus accesos de internet en un año.
def piechart_anio(datos: pd.DataFrame, anio:int)->None: 
    #creo un copia del DataFrame para filtrar solo los datos que necesito.
    copia=datos[["AÑO","DEPARTAMENTO", "No. ACCESOS FIJOS"]].copy()
    #Comparar el año dentro de la copia con al año que ingresa por parametro.
    datos_anio = datos[copia["AÑO"] == anio]
    # Agrupar por departamento y contar los accesos
    accesos_por_departamento = datos_anio.groupby("DEPARTAMENTO")["No. ACCESOS FIJOS"].sum()
    # Obtener el top 20 departamentos
    top_20_departamentos = accesos_por_departamento.nlargest(20)
    top_20_departamentos.plot(kind="pie",autopct="%0.1f%%",figsize=(10,8), title="Top 20 Departamentos con Accesos Fijos a Internet en "+ str(anio))
    # Mostrar el plot
    plot.show()    
#piechart_anio(datos, 2021)
 
#Requerimiento 2(listo)
def diagrama_barras(datos: pd.DataFrame, Departamento: str)->None:
    #Crear una copia del DataFrame
    copia=datos.copy()
    #Se compara el Departamento que ingresa por parametro y el que esta dentro de copia del DataFrame
    datos_filtrados = datos[copia["DEPARTAMENTO"] == Departamento]
    #Agrupo los Municipios.
    agrupaciones=datos_filtrados.groupby("MUNICIPIO")    
    suma1 = agrupaciones["No. ACCESOS FIJOS"].sum()
    suma2 = agrupaciones["POBLACIÓN DANE"].sum()
    #realizaos una división de las dos sumas que se realizaro anteriormente.
    division = (suma1/suma2).sort_values(ascending=False)
    # Obtener el top 20 departamentos
    top_20_departamentos = division.head(20)
    top_20_departamentos.plot(kind="bar", figsize=(13,7), fontsize="small", ylim=(0.0,0.40), title="Top 20 municipios con mayor relación de Accesos Fijos a internet por población en " + Departamento , ylabel=("Relación accesos fijos a internet por población"), xlabel=" Municipios de" + Departamento)
    
    # Mostrar el plot
    plot.show()
#diagrama_barras(datos, "Santander") 
   
#Requerimiento 3(listo)
def diagrama_cajas(datos: pd.DataFrame, Departamento: str) -> None:
    """Genera un diagrama de caja y bigotes que muestra la distribución de accesos fijos a internet por provincia en un departamento específico.
    
    Parámetros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
        departamento (str): El nombre del departamento para el cual se generará el gráfico.
    """
    #Se hizo un copia del DataFrame que ingresa como parametro.
    copia=datos[["PROVINCIA","DEPARTAMENTO", "No. ACCESOS FIJOS"]].copy()
    # Filtrar los datos para el departamento especificado
    datos_filtrados = datos[copia["DEPARTAMENTO"] == Departamento]
    segundo_filtro = datos_filtrados[["PROVINCIA","No. ACCESOS FIJOS"]]
    provincia=segundo_filtro.groupby("PROVINCIA")
    
    # Crear el diagrama de caja y bigotes
    provincia.boxplot(figsize=(14, 8),vert=False, by="PROVINCIA", showfliers=False,sharey=False)

    # Ajustar el título y etiquetas
    plot.title("Diagrama de caja de accesos fijos por provincias en el departamento de "+ Departamento)
    plot.suptitle("")  # Eliminar el título por defecto generado por `pandas`
    plot.ylabel("No. ACCESOS FIJOS")
    plot.xlabel("No. de accesos fijos a internet") 
    plot.xticks(rotation=45, fontsize='small')  # Ajustar la rotación y el tamaño de la fuente de las etiquetas del eje x
    
    # Ajustar el espacio entre subplots
    plot.subplots_adjust(hspace=0.4, left=0.2)
    
    # Mostrar el plot
    plot.show()

#diagrama_cajas(datos, "Cauca")
    
# Parte 3
#Requerimiento 4(listo)
def crear_matriz(datos: pd.DataFrame)->tuple:
    #Esqueleto diccionarios
    deptos =  sorted(datos["DEPARTAMENTO"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    anios =  sorted(datos["AÑO"].unique())
    anios_dict = dict(list(enumerate(anios)))
    #TODO completar la construcción de la matriz
    matriz_final=[]
    for i in dept_dict:
        fila_vacia=[]
        depto = dept_dict[i]
        filtro_depto= datos[datos["DEPARTAMENTO"]==depto] 
        for j in anios_dict:
            anio=anios_dict[j]
            #Comparar el año dentro del primer fltro con el año que ingresa por parametro.
            filtro_anio=filtro_depto[filtro_depto["AÑO"]==anio] 
            fila_vacia.append(filtro_anio["No. ACCESOS FIJOS"].sum())
        matriz_final.append(fila_vacia)

    return (matriz_final, anios_dict, dept_dict)

#Requerimiento 5
def cantidad_accesos_anio(matriz: tuple, anio:int, datos: pd.DataFrame)-> int:
   # n debe retornar el valor que representa la cantidad de accesos fijos totales en el año dado por el usuario
   matriz_1=crear_matriz(cargar_datos("Internet.csv"))
   suma=0
   casilla=matriz_1[1]
   pos_fila=None
   for i in casilla: # range(0,len(matriz[0])):
       dato=casilla[i]
       if dato==anio: # matriz[0][i]==anio:
            pos_fila=i
   matriz_2=matriz_1
   for j in matriz_2: #range(1,len(matriz)):
       str(suma)+=str(j[pos_fila])
   return int(suma)




#Requerimiento 6
def departamento_en_ascenso(matriz: tuple, anio: int, porcentaje: float, datos: pd.DataFrame)->tuple:
   #Comparar el año dentro de la copia con al año que ingresa por parametro.
    datos_filtrados = datos[datos["AÑO"] == anio]
    if anio>= 2023 or anio<2015:
        return ("Ninguno",-101)
    tupla_1=[]
    # orden alfabético
    orden_dept =  sorted(datos["DEPARTAMENTO"].unique())
    matriz_final, anios_dict, dept_dict=matriz 
    #compara el año qu epaa por parametro con el que se encuentra en datos(el DataFrame)
    # Excluir el último año
    anio_s= anio+1
    accesos_anio_s= "accesos_anio"+anio_s
    departamento_con_mayor_crecimiento = ""
    porcentaje_superado = 0
    for i in orden_dept:
       # revision=
        cambio_porcentual = ("""acessos del anio_s -acessos del anio""") / 100
        if cambio_porcentual > porcentaje:
            departamento_mayor_crecimiento = ["DEPARTAMENTO"]
            porcentaje_superado = cambio_porcentual
    tupla_1.append(departamento_mayor_crecimiento, porcentaje_superado)
    return tupla_1
    
    

    orden_anios =  sorted(datos["AÑO"].unique())
    
    if anio==-1:
        respuesta=("Ninguno",-101)
        return respuesta


"""
import matplotlib.image as mpimg
def ejecutar_departamentos_mapa(matriz: tuple):
    def cargar_coordenadas(nombre_archivo: str) -> dict:
        deptos = {}
        with open(nombre_archivo, encoding="utf8") as archivo:
            archivo.readline()  # Omitir la línea de títulos
            for linea in archivo:
                linea = linea.strip()
                datos = linea.split(";")
                deptos[datos[0]] = (int(datos[1]), int(datos[2]))
        return deptos
    
    def mapa_accesos_fijos(matriz:tuple, anio:int, coordenadas:str):
        mapa = mpimg.imread("mapa.png").tolist()
        colores = {"0 a <5000": [0.94, 0.10, 0.10],
                   "5000 a <10000": [0.94, 0.10, 0.85],
                   "10000 a <20000": [0.10, 0.50, 0.94],
                   "20000 a <500000": [0.34, 0.94, 0.10],
                   ">=500000": [0.99, 0.82, 0.09]}
    
        # Obtener el diccionario de columnas
        dict_columnas = matriz[1]
        col_anio = -1
        for i in range(len(dict_columnas)):
            if dict_columnas[i] == anio:
                col_anio = i

    if col_anio == -1:
        print("No se encontraron datos para el año" + str(anio))
        return
    
 #Poner colores segun el rango
        for depto, coord in coordenadas.items():
            accesos = matriz[0][matriz[2][depto]][col_anio]
            for i in range(13):
                for j in range(13):
                    x = coord[0] - 6 + j
                    y = coord[1] - 6 + i
                    if 0 <= accesos < 5000:
                        mapa[y][x] = colores["0 a <5000"]
                    elif 5000 <= accesos < 10000:
                        mapa[y][x] = colores["5000 a <10000"]
                    elif 10000 <= accesos < 20000:
                        mapa[y][x] = colores["10000 a <20000"]
                    elif 20000 <= accesos < 500000:
                        mapa[y][x] = colores["20000 a <500000"]
                    else:
                        mapa[y][x] = colores[">=500000"]
    
        plt.imshow(mapa)
        legends = []
        for rango in colores:
            legends.append(mpatches.Patch(color=colores[rango], label=rango))
        plt.legend(handles=legends, loc=3, fontsize='x-small')
        plt.title(f"Accesos fijos a internet por departamento en el año {anio}", fontsize='x-small')
        plt.show()
    
    # Ejemplo de uso
    matriz = (... , ... , ...)  # Tupla con la matriz y los diccionarios
    anio = 2020
    coordenadas = cargar_coordenadas("coordenadas.txt")
    mapa_accesos_fijos(matriz, anio, coordenadas)
    """
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Acceso a internet en Colombia
Interfaz basada en consola para la interaccion con el usuario.

@author: Cupi2
"""

import internet as mod
import pandas as pd
import matplotlib.pyplot as plot

def ejecutar_cargar_datos() -> pd.DataFrame:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos del acceso a internet en Colombia.
    Retorno: dataframe
        El dataframe con los datos cargados del archivo CSV.
    """
    datos = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la informacion del acceso a internet en Colombia: ")
    datos = mod.cargar_datos(archivo)
    if len(datos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la informacion.")
    else:
        print("Se cargaron los siguientes datos a partir del archivo csv: ")
        print(datos)
    return datos

def ejecutar_piechart_anio(datos:pd.DataFrame, anio:int )->None:
    """Solicita al usuario que ingrese un anio y muestra un piechart con la distribucion de accesos fijos a internet por departamento.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    anio=int(input("Ingrese un año: "))
    print(mod.piechart_anio(datos, anio))
    
def ejecutar_diagrama_barras(datos: pd.DataFrame, Departamento: str)->None:
    """Muestra un diagrama de barras con la relacion entre el numero de accesos fijos a internet y la poblacion por municipio.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    Departamento=input("Ingrese un departamento: ")
    print(mod.diagrama_barras(datos,Departamento))
   
   
   
def ejecutar_diagrama_cajas(datos: pd.DataFrame,Departamento: str):
    """Muestra un diagrama de cajas con la distribucion de accesos fijos a internet por provincia en un departamento.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    Departamento=input("Ingrese un departamento: ")
    print(mod.diagrama_cajas(datos, Departamento))
    
def crear_matriz(datos: pd.DataFrame)->tuple:
    """Crea una matriz con la cantidad de accesos fijos a internet por departamento y anio.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    Retorno: tuple
        La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    matriz = mod.crear_matriz(datos)
    print("Se ha creado la matriz con la cantidad de accesos fijos a internet por departamento y anio.")
    print (matriz)
    return matriz

    
def ejecutar_cantidad_accesos_anio(matriz: tuple,anio:int, datos: pd.DataFrame)->int:
    """Muestra la cantidad de accesos fijos a internet en un anio.
    Parametros:
        matriz (tuple): La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    anio=int(input("Porfavor ingrese un año: "))
    print("La cantidad de accesos fijos a internet en el año " + str(anio) + " es de " + str(mod.cantidad_accesos_anio(matriz,anio,datos)))
   
def ejecutar_departamento_en_ascenso(matriz: tuple,anio:int, porcentaje: float,  datos: pd.DataFrame)->tuple:
    """Muestra el primer departamento que supera el porcentaje de incremento de accesos fijos a internet en un anio dado.
    Parametros:
        matriz (tuple): La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    anio=input("Porfavor ingrese un año: ")
    porcentaje=input("Porfavor ingrese un porcentaje por el cual desee comparar: ")
    llamar=print(mod.departamento_en_ascenso(matriz, anio, porcentaje, datos))
    #if llamar(departamento_mayor_crecimiento)!=("Ninguno",-101) :
        #respuesta=print(llamar(departamento_mayor_crecimiento) +" tuvo un crecimiento del " + llamar(round(porcentaje_superior),2) + "% del año " + str(anio) + " al año " + str(anio+1))
   # else:
       # respuesta=print("No se encontró ningún departamento que supere el porcentaje especificado.")

   
           
    
def ejecutar_departamentos_mapa(matriz: tuple):
    """Genera un mapa con la cantidad de accesos fijos a internet por departamento en un anio.
    Parametros:
        matriz (tuple): La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    #Complete la siguiente función solamente si desea implementar el bono 
    #TODO Completar?


def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar datos sobre el acceso a internet en Colombia.") 
    print("2. Mostrar Top 20 departamentos con mayor numero de accesos fijos a internet en un anio.") 
    print("3. Mostrar Top 20 municipios con mayor numero de accesos fijos por población en un departamento. ")
    print("4. Mostrar diagrama de cajas con la distribucion de accesos fijos a internet por provincia en un departamento.")
    print("5. Construir matriz de Departamentos vs Año.")
    print("6. Consultar la cantidad de accesos fijos a internet en un anio.")
    print("7. Consultar si existe un departamento en ascenso en un anio dado.")
    #Descomente la siguiente línea si desea implementar el bono. 
    #print("8. Generar mapa de la cantidad de accesos fijos a internet por departamento en un anio.")
    print("9. Salir.")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    datos = ""
    anio=0
    Departamento=""
    porcentaje=0
    matriz = []
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opcion: "))
        if opcion_seleccionada == 1:
            datos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_piechart_anio(datos,anio)
        elif opcion_seleccionada == 3:
            ejecutar_diagrama_barras(datos,Departamento)
        elif opcion_seleccionada == 4:
            ejecutar_diagrama_cajas(datos, Departamento)
        elif opcion_seleccionada == 5:
            matriz = crear_matriz(datos)
        elif opcion_seleccionada == 6:
            ejecutar_cantidad_accesos_anio(matriz, anio , datos)
        elif opcion_seleccionada == 7:
            ejecutar_departamento_en_ascenso(matriz,anio, porcentaje)
        #Descomente las siguientes dos líneas si desea implementar el bono. 
        #elif opcion_seleccionada == 8:
            #ejecutar_departamentos_mapa(matriz)
        elif opcion_seleccionada == 9:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

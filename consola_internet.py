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

def ejecutar_piechart_anio(datos: pd.DataFrame, anio: int) -> None:
    """Solicita al usuario que ingrese un anio y muestra un piechart con la distribucion de accesos fijos a internet por departamento.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
        anio (int): El año para el cual se quiere generar el pie chart.
    """
    if datos is not None and not datos.empty:
        mod.piechart_anio(datos, anio)
    else:
        print("No se han cargado datos. Por favor cargue los datos primero.")

def ejecutar_diagrama_barras(datos: pd.DataFrame, departamento: str) -> None:
    """Muestra un diagrama de barras con la relacion entre el numero de accesos fijos a internet y la poblacion por municipio.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
        departamento (str): El departamento para el cual se quiere generar el diagrama de barras.
    """
    if datos is not None and not datos.empty:
        mod.diagrama_barras(datos, departamento)
    else:
        print("No se han cargado datos. Por favor cargue los datos primero.")

def ejecutar_diagrama_cajas(datos: pd.DataFrame, departamento: str) -> None:
    """Muestra un diagrama de cajas con la distribucion de accesos fijos a internet por provincia en un departamento.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
        departamento (str): El departamento para el cual se quiere generar el diagrama de cajas.
    """
    if datos is not None and not datos.empty:
        mod.diagrama_cajas(datos, departamento)
    else:
        print("No se han cargado datos. Por favor cargue los datos primero.")

def crear_matriz(datos: pd.DataFrame) -> tuple:
    """Crea una matriz con la cantidad de accesos fijos a internet por departamento y anio.
    Parametros:
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    Retorno: tuple
        La matriz con la cantidad de accesos fijos a internet por departamento y anio.
    """
    if datos is not None and not datos.empty:
        matriz = mod.crear_matriz(datos)
        print("Se ha creado la matriz con la cantidad de accesos fijos a internet por departamento y anio.")
        return matriz
    else:
        print("No se han cargado datos. Por favor cargue los datos primero.")
        return ([], {}, {})

def ejecutar_cantidad_accesos_anio(matriz: tuple, anio: int, datos: pd.DataFrame) -> None:
    """Muestra la cantidad de accesos fijos a internet en un anio.
    Parametros:
        matriz (tuple): La matriz con la cantidad de accesos fijos a internet por departamento y anio.
        anio (int): El año para el cual se quiere consultar la cantidad de accesos.
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    if matriz and anio in matriz[1].values():
        cantidad = mod.cantidad_accesos_anio(matriz, anio, datos)
        print(f"La cantidad de accesos fijos a internet en el año {anio} es de {cantidad}.")
    else:
        print("No se ha creado la matriz o el año no es válido. Por favor cargue los datos y cree la matriz primero.")

def ejecutar_departamento_en_ascenso(matriz: tuple, anio: int, porcentaje: float, datos: pd.DataFrame) -> None:
    """Muestra el primer departamento que supera el porcentaje de incremento de accesos fijos a internet en un anio dado.
    Parametros:
        matriz (tuple): La matriz con la cantidad de accesos fijos a internet por departamento y anio.
        anio (int): El año para el cual se quiere verificar el ascenso.
        porcentaje (float): El porcentaje de incremento a verificar.
        datos (pd.DataFrame): El dataframe con los datos del acceso a internet en Colombia.
    """
    if matriz and anio in matriz[1].values():
        resultado = mod.departamento_en_ascenso(matriz, anio, porcentaje, datos)
        if resultado != ("Ninguno", -101):
            print(f"{resultado[0]} tuvo un crecimiento del {round(resultado[1], 2)}% del año {anio} al año {anio+1}.")
        else:
            print("No se encontró ningún departamento que supere el porcentaje especificado.")
    else:
        print("No se ha creado la matriz o el año no es válido. Por favor cargue los datos y cree la matriz primero.")

def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario."""
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
    datos = pd.DataFrame()
    matriz = ()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opcion: "))
        if opcion_seleccionada == 1:
            datos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            anio = int(input("Ingrese un año: "))
            ejecutar_piechart_anio(datos, anio)
        elif opcion_seleccionada == 3:
            departamento = input("Ingrese un departamento: ")
            ejecutar_diagrama_barras(datos, departamento)
        elif opcion_seleccionada == 4:
            departamento = input("Ingrese un departamento: ")
            ejecutar_diagrama_cajas(datos, departamento)
        elif opcion_seleccionada == 5:
            matriz = crear_matriz(datos)
        elif opcion_seleccionada == 6:
            anio = int(input("Por favor ingrese un año: "))
            ejecutar_cantidad_accesos_anio(matriz, anio, datos)
        elif opcion_seleccionada == 7:
            anio = int(input("Por favor ingrese un año: "))
            porcentaje = float(input("Por favor ingrese un porcentaje por el cual desee comparar: "))
            ejecutar_departamento_en_ascenso(matriz, anio, porcentaje, datos)
        #Descomente las siguientes dos líneas si desea implementar el bono. 
        #elif opcion_seleccionada == 8:
            #ejecutar_departamentos_mapa(matriz)
        elif opcion_seleccionada == 9:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")

# PROGRAMA PRINCIPAL
iniciar_aplicacion()

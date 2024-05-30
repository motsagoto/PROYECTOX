# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Acceso a internet en Colombia
Modulo de funciones.

@author: Cupi2
"""
import pandas as pd
import matplotlib.pyplot as plt

# Parte 1 (listo)
def cargar_datos(archivo: str) -> pd.DataFrame:
    """Carga los datos de un archivo CSV y los retorna como un DataFrame."""
    return pd.read_csv(archivo, sep=",")

# Parte 2
# Requerimiento 1 (listo)
def piechart_anio(datos: pd.DataFrame, anio: int) -> None:
    """Genera un gráfico de pastel de los 20 departamentos con más accesos fijos a internet en un año dado."""
    datos_anio = datos[datos["AÑO"] == anio]
    accesos_por_departamento = datos_anio.groupby("DEPARTAMENTO")["No. ACCESOS FIJOS"].sum()
    top_20_departamentos = accesos_por_departamento.nlargest(20)
    top_20_departamentos.plot(kind="pie", autopct="%0.1f%%", figsize=(10, 8), title="Top 20 Departamentos con Accesos Fijos a Internet en " + str(anio))
    plt.ylabel("")
    plt.show()

# Requerimiento 2 (listo)
def diagrama_barras(datos: pd.DataFrame, departamento: str) -> None:
    """Genera un diagrama de barras de los 20 municipios con mayor relación de accesos fijos a internet por población en un departamento dado."""
    datos_filtrados = datos[datos["DEPARTAMENTO"] == departamento]
    agrupaciones = datos_filtrados.groupby("MUNICIPIO")
    suma1 = agrupaciones["No. ACCESOS FIJOS"].sum()
    suma2 = agrupaciones["POBLACIÓN DANE"].sum()
    division = (suma1 / suma2).sort_values(ascending=False)
    top_20_municipios = division.head(20)
    top_20_municipios.plot(kind="bar", figsize=(13, 7), fontsize="small", ylim=(0.0, 0.40), title="Top 20 municipios con mayor relación de Accesos Fijos a internet por población en " + departamento, ylabel="Relación accesos fijos a internet por población", xlabel="Municipios de " + departamento)
    plt.show()

# Requerimiento 3 (listo)
def diagrama_cajas(datos: pd.DataFrame, departamento: str) -> None:
    """Genera un diagrama de cajas de los accesos fijos a internet por provincia en un departamento dado."""
    datos_filtrados = datos[datos["DEPARTAMENTO"] == departamento]
    datos_provincia = datos_filtrados[["PROVINCIA", "No. ACCESOS FIJOS"]]
    datos_provincia.boxplot(by="PROVINCIA", showfliers=False, vert=False, figsize=(14, 8))
    plt.title("Diagrama de caja de accesos fijos por provincias en el departamento de " + departamento)
    plt.suptitle("")
    plt.ylabel("No. ACCESOS FIJOS")
    plt.xlabel("No. de accesos fijos a internet")
    plt.xticks(rotation=45, fontsize='small')
    plt.subplots_adjust(hspace=0.4, left=0.2)
    plt.show()

# Parte 3
# Requerimiento 4 (listo)
def crear_matriz(datos: pd.DataFrame) -> tuple:
    """Crea una matriz de accesos fijos a internet por departamento y año."""
    deptos = sorted(datos["DEPARTAMENTO"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    anios = sorted(datos["AÑO"].unique())
    anios_dict = dict(list(enumerate(anios)))
    matriz_final = []
    for i in dept_dict:
        fila_vacia = []
        depto = dept_dict[i]
        filtro_depto = datos[datos["DEPARTAMENTO"] == depto]
        for j in anios_dict:
            anio = anios_dict[j]
            filtro_anio = filtro_depto[filtro_depto["AÑO"] == anio]
            fila_vacia.append(filtro_anio["No. ACCESOS FIJOS"].sum())
        matriz_final.append(fila_vacia)
    return (matriz_final, anios_dict, dept_dict)

# Requerimiento 5 (listo)
def cantidad_accesos_anio(matriz: tuple, anio: int) -> int:
    """Calcula la cantidad total de accesos fijos a internet en un año dado."""
    _, anios_dict, _ = matriz
    pos_anio = next((key for key, value in anios_dict.items() if value == anio), None)
    if pos_anio is None:
        return 0
    return sum(fila[pos_anio] for fila in matriz[0])

# Requerimiento 6 (listo)
def departamento_en_ascenso(matriz: tuple, anio: int, porcentaje: float) -> tuple:
    """Determina el departamento con el mayor crecimiento en accesos fijos a internet entre dos años consecutivos."""
    if anio >= 2023 or anio < 2015:
        return ("Ninguno", -101)
    matriz_final, anios_dict, dept_dict = matriz
    pos_anio = next((key for key, value in anios_dict.items() if value == anio), None)
    if pos_anio is None or pos_anio + 1 not in anios_dict:
        return ("Ninguno", -101)
    max_cambio = ("Ninguno", -101)
    for i in range(len(dept_dict)):
        if matriz_final[i][pos_anio] == 0:
            continue
        crecimiento = (matriz_final[i][pos_anio + 1] - matriz_final[i][pos_anio]) / matriz_final[i][pos_anio] * 100
        if crecimiento > porcentaje and crecimiento > max_cambio[1]:
            max_cambio = (dept_dict[i], crecimiento)
    return max_cambio

# Funciones de ejecución
def ejecutar_cargar_datos() -> pd.DataFrame:
    archivo = input("Por favor ingrese el nombre del archivo CSV: ")
    return cargar_datos(archivo)

def ejecutar_piechart_anio(datos: pd.DataFrame, anio: int) -> None:
    anio = int(input("Por favor ingrese un año: "))
    piechart_anio(datos, anio)

def ejecutar_diagrama_barras(datos: pd.DataFrame, departamento: str) -> None:
    departamento = input("Por favor ingrese un departamento: ")
    diagrama_barras(datos, departamento)

def ejecutar_diagrama_cajas(datos: pd.DataFrame, departamento: str) -> None:
    departamento = input("Por favor ingrese un departamento: ")
    diagrama_cajas(datos, departamento)

def ejecutar_crear_matriz(datos: pd.DataFrame) -> tuple:
    matriz = crear_matriz(datos)
    print("Se ha creado la matriz con la cantidad de accesos fijos a internet por departamento y año.")
    return matriz

def ejecutar_cantidad_accesos_anio(matriz: tuple) -> None:
    anio = int(input("Por favor ingrese un año: "))
    print("La cantidad de accesos fijos a internet en el año " + str(anio) + " es de " + str(cantidad_accesos_anio(matriz, anio)))

def ejecutar_departamento_en_ascenso(matriz: tuple) -> None:
    anio = int(input("Por favor ingrese un año: "))
    porcentaje = float(input("Por favor ingrese un porcentaje: "))
    departamento, crecimiento = departamento_en_ascenso(matriz, anio, porcentaje)
    if departamento != "Ninguno":
        print(departamento + " tuvo un crecimiento del " + str(round(crecimiento, 2)) + "% del año " + str(anio) + " al año " + str(anio + 1))
    else:
        print("No se encontró ningún departamento que supere el porcentaje especificado.")

def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario."""
    print("\nOpciones")
    print("1. Cargar datos sobre el acceso a internet en Colombia.")
    print("2. Mostrar Top 20 departamentos con mayor numero de accesos fijos a internet en un año.")
    print("3. Mostrar Top 20 municipios con mayor numero de accesos fijos por población en un departamento.")
    print("4. Mostrar diagrama de cajas con la distribución de accesos fijos a internet por provincia en un departamento.")
    print("5. Construir matriz de Departamentos vs Año.")
    print("6. Consultar la cantidad de accesos fijos a internet en un año.")
    print("7. Consultar si existe un departamento en ascenso en un año dado.")
    print("8. Salir.")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    datos = None
    matriz = None
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            datos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2 and datos is not None:
            ejecutar_piechart_anio(datos, 0)
        elif opcion_seleccionada == 3 and datos is not None:
            ejecutar_diagrama_barras(datos, "")
        elif opcion_seleccionada == 4 and datos is not None:
            ejecutar_diagrama_cajas(datos, "")
        elif opcion_seleccionada == 5 and datos is not None:
            matriz = ejecutar_crear_matriz(datos)
        elif opcion_seleccionada == 6 and matriz is not None:
            ejecutar_cantidad_accesos_anio(matriz)
        elif opcion_seleccionada == 7 and matriz is not None:
            ejecutar_departamento_en_ascenso(matriz)
        elif opcion_seleccionada == 8:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

# PROGRAMA PRINCIPAL
iniciar_aplicacion()

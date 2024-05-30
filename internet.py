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
    """
    Calcula la cantidad total de accesos fijos a internet en un año dado.

    Parámetros:
    matriz (tuple): Tupla que contiene la matriz de datos y los diccionarios de años y departamentos.
    anio (int): Año para el cual se quiere calcular la cantidad de accesos fijos.

    Retorna:
    int: Cantidad total de accesos fijos a internet en el año dado.
    """
    _, anios_dict, _ = matriz

    # Encontrar la posición del año en el diccionario anios_dict
    pos_anio = None
    for key, value in anios_dict.items():
        if value == anio:
            pos_anio = key
            break

    # Si no se encuentra el año en el diccionario, retorna 0.
    if pos_anio is None:
        return 0

    # Suma los accesos fijos de todas las filas (departamentos) en la columna correspondiente al año buscado.
    return sum(fila[pos_anio] for fila in matriz[0])

# Requerimiento 6 (listo y corregido)
def departamento_en_ascenso(matriz: tuple, anio: int, porcentaje: float) -> tuple:
    """
    Determina el departamento con el mayor crecimiento en accesos fijos a internet entre dos años consecutivos.

    Parámetros:
    matriz (tuple): Tupla que contiene la matriz de datos y los diccionarios de años y departamentos.
    anio (int): Año base para calcular el crecimiento.
    porcentaje (float): Porcentaje mínimo de crecimiento.

    Retorna:
    tuple: Nombre del departamento y el porcentaje de crecimiento. Si no se encuentra ninguno, retorna ("Ninguno", -101).
    """
    if anio >= 2023 or anio < 2015:
        return ("Ninguno", -101)

    matriz_final, anios_dict, dept_dict = matriz

    # Encontrar la posición del año en el diccionario anios_dict
    pos_anio = None
    for key, value in anios_dict.items():
        if value == anio:
            pos_anio = key
            break

    # Verifica si se encontró el año y si hay un año siguiente en el diccionario.
    if pos_anio is None or pos_anio + 1 not in anios_dict:
        return ("Ninguno", -101)

    max_cambio = ("Ninguno", -101)

    # Itera sobre cada fila (departamento) en la matriz de datos.
    for i in range(len(dept_dict)):
        accesos_anio_base = matriz_final[i][pos_anio]
        accesos_anio_siguiente = matriz_final[i][pos_anio + 1]

        # Si el número de accesos fijos en el año base es mayor a 0, calcula el crecimiento.
        if accesos_anio_base != 0:
            # Cálculo del crecimiento porcentual de accesos fijos a internet.
            crecimiento = ((accesos_anio_siguiente - accesos_anio_base) / accesos_anio_base) * 100

            # Si el crecimiento es mayor al porcentaje especificado y es el mayor registrado, actualiza max_cambio.
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
    resultado = departamento_en_ascenso(matriz, anio, porcentaje)
    print("El departamento con mayor crecimiento en accesos fijos a internet es: " + resultado[0] + " con un crecimiento del " + str(resultado[1]) + "%.")

def menu() -> None:
    datos = None
    matriz = None
    while True:
        print("\n--- Menú ---")
        print("1. Cargar datos")
        print("2. Generar gráfico de pastel por año")
        print("3. Generar diagrama de barras por departamento")
        print("4. Generar diagrama de cajas por departamento")
        print("5. Crear matriz de accesos fijos a internet")
        print("6. Calcular cantidad de accesos fijos a internet en un año")
        print("7. Determinar departamento en ascenso")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = ejecutar_cargar_datos()
        elif opcion == "2":
            if datos is not None:
                ejecutar_piechart_anio(datos, 0)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "3":
            if datos is not None:
                ejecutar_diagrama_barras(datos, "")
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "4":
            if datos is not None:
                ejecutar_diagrama_cajas(datos, "")
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "5":
            if datos is not None:
                matriz = ejecutar_crear_matriz(datos)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "6":
            if matriz is not None:
                ejecutar_cantidad_accesos_anio(matriz)
            else:
                print("Primero debe crear la matriz.")
        elif opcion == "7":
            if matriz is not None:
                ejecutar_departamento_en_ascenso(matriz)
            else:
                print("Primero debe crear la matriz.")
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    menu()

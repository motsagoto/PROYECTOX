# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Acceso a internet en Colombia
Modulo de funciones.

@author: Cupi2
"""
import pandas as pd
import matplotlib.pyplot as plot

#Parte 1 (listo)
def cargar_datos(archivo: str) -> pd.DataFrame:
    llamar = pd.read_csv(archivo, sep=",")
    return llamar
datos = cargar_datos("internet.csv")

# Parte 2
# Requerimiento 1 (listo)
def piechart_anio(datos: pd.DataFrame, anio: int) -> None:
    copia = datos[["AÑO", "DEPARTAMENTO", "No. ACCESOS FIJOS"]].copy()
    datos_anio = copia[copia["AÑO"] == anio]
    accesos_por_departamento = datos_anio.groupby("DEPARTAMENTO")["No. ACCESOS FIJOS"].sum()
    top_20_departamentos = accesos_por_departamento.nlargest(20)
    top_20_departamentos.plot(kind="pie", autopct="%0.1f%%", figsize=(10, 8), title="Top 20 Departamentos con Accesos Fijos a Internet en " + str(anio))
    plot.show()
 
# Requerimiento 2 (listo)
def diagrama_barras(datos: pd.DataFrame, departamento: str) -> None:
    copia = datos.copy()
    datos_filtrados = copia[copia["DEPARTAMENTO"] == departamento]
    agrupaciones = datos_filtrados.groupby("MUNICIPIO")    
    suma1 = agrupaciones["No. ACCESOS FIJOS"].sum()
    suma2 = agrupaciones["POBLACIÓN DANE"].sum()
    division = (suma1 / suma2).sort_values(ascending=False)
    top_20_departamentos = division.head(20)
    top_20_departamentos.plot(kind="bar", figsize=(13, 7), fontsize="small", ylim=(0.0, 0.40), title="Top 20 municipios con mayor relación de Accesos Fijos a internet por población en " + departamento, ylabel="Relación accesos fijos a internet por población", xlabel="Municipios de " + departamento)
    plot.show()

# Requerimiento 3 (listo)
def diagrama_cajas(datos: pd.DataFrame, departamento: str) -> None:
    copia = datos[["PROVINCIA", "DEPARTAMENTO", "No. ACCESOS FIJOS"]].copy()
    datos_filtrados = copia[copia["DEPARTAMENTO"] == departamento]
    segundo_filtro = datos_filtrados[["PROVINCIA", "No. ACCESOS FIJOS"]]
    provincia = segundo_filtro.groupby("PROVINCIA")
    provincia.boxplot(figsize=(14, 8), vert=False, by="PROVINCIA", showfliers=False, sharey=False)
    plot.title("Diagrama de caja de accesos fijos por provincias en el departamento de " + departamento)
    plot.suptitle("")
    plot.ylabel("No. ACCESOS FIJOS")
    plot.xlabel("No. de accesos fijos a internet") 
    plot.xticks(rotation=45, fontsize='small')
    plot.subplots_adjust(hspace=0.4, left=0.2)
    plot.show()

# Parte 3
# Requerimiento 4 (listo)
def crear_matriz(datos: pd.DataFrame) -> tuple:
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

# Requerimiento 5
def cantidad_accesos_anio(matriz: tuple, anio: int, datos: pd.DataFrame) -> int:
    _, anios_dict, _ = matriz
    pos_anio = None
    for key, value in anios_dict.items():
        if value == anio:
            pos_anio = key
            break
    if pos_anio is None:
        return 0
    total_accesos = sum(fila[pos_anio] for fila in matriz[0])
    return total_accesos

# Requerimiento 6
def departamento_en_ascenso(matriz: tuple, anio: int, porcentaje: float, datos: pd.DataFrame) -> tuple:
    if anio >= 2023 or anio < 2015:
        return ("Ninguno", -101)
    matriz_final, anios_dict, dept_dict = matriz
    pos_anio = None
    for key, value in anios_dict.items():
        if value == anio:
            pos_anio = key
            break
    if pos_anio is None or pos_anio + 1 not in anios_dict:
        return ("Ninguno", -101)
    max_cambio = ("Ninguno", -101)
    for i in range(len(dept_dict)):
        if matriz_final[i][pos_anio] == 0:
            continue
        crecimiento = (matriz_final[i][pos_anio + 1] - matriz_final[i][pos_anio]) / matriz_final[i][pos_anio] * 100
        if crecimiento > porcentaje:
            max_cambio = (dept_dict[i], crecimiento)
            break
    return max_cambio

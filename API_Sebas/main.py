# Lector / Visualizador de Informacion financiera
import requests

# Armado del Request

# dias = 1 # Fijar días habiles sin fin de semana.

# for idias in range(dias):
#     pedidoIntro = "https://api.polygon.io/v2/aggs/ticker/"
#     pedidoTicker = "AAPL"
#     pedidoCont = "/range/1/day/"
#     pedidoDate1 = "2021-07-0"
#     pedidoDate2 = "/2021-07-0"
#     pedidoLen = str(idias+5)
#     pedidoClosure = "?adjusted=true&sort=asc&limit=120&apiKey=umyzeMtyrZdVcXUxxb3mtZ5ZSnoFA4O1"
#
#     print(https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey=umyzeMtyrZdVcXUxxb3mtZ5ZSnoFA4O1)

    # Request

json_file = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey=umyzeMtyrZdVcXUxxb3mtZ5ZSnoFA4O1")

print(json_file.text)

json_obj = json_file.json() # Parseo a Diccionario de Python

ticker = json_obj["ticker"]
value = json_obj["results"]

print(ticker)
print(value)

print(f"Ticker: {ticker} - {value[0]['v']}")

# def stock_analyzer(name):

# https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey=umyzeMtyrZdVcXUxxb3mtZ5ZSnoFA4O1


# TP Final Certificación Profesional Python
# Resumen
# Se pide implementar un programa que permita leer datos de una API de finanzas, guardarlos en una base de datos y graficarlos.
#
# Entrega
# Fecha límite 30 de septiembre.
#
# El trabajo se entrega en grupos de hasta 5 personas y se piden lo siguientes entregables:
#
# Informe de funcionalidad y diseño
# Repositorio de github
# Detalles de implementación
# Menú principal
# El programa debe presentar un menú principal donde puedan elegirse las siguientes dos opciones:
#
# Actualización de datos
# Visualización de datos
# Actualización de datos
# El programa debe solicitar al usuario el valor de un ticker, una fecha de inicio y una fecha de fin. Debe luego pedir los valores a la API y guardar estos datos en una base de datos SQL.
#
# Ejemplo:
#
# >>> Ingrese ticker a pedir:
# AAPL
# >>> Ingrese fecha de inicio:
# 2022/01/01
# >>> Ingrese fecha de fin:
# 2022/07/01
# >>> Pidiendo datos ...
# >>> Datos guardados correctamente
# Visualización de datos
# El programa debe permitir dos visualizaciones de datos:
#
# Resumen
# Gráfico de ticker
# Resumen
# Debe imprimir un resumen de los datos guardados en la base de datos.
#
# Ejemplos:
#
# >>> Los tickers guardados en la base de datos son:
# >>> AAPL - 2022/01/01 <-> 2022/07/01
# >>> AAL  - 2021/01/01 <-> 2022/07/01
# Gráfico
# El programa debe permitir graficar los datos guardados para un ticker específico.
#
# Ejemplo:
#
# >>> Ingrese el ticker a graficar:
# AAL
# Condición de aprobación
# El programa debe cumplir con toda la funcionalidad dentro de detalles de implementación. Para obtener una nota superior a 7 deben implementarse alguna funcionalidad extra, sea las propuestas o propuestas por el grupo.
#
# Extras
# Posibles extras para el programa:
#
# Visualización en tiempo real del valor de una acción.
# Actualización de rangos en base de datos considerando lo guardado. Ej: Si tengo del 2022/01/01 al 2022/07/01 y pido del 2021/01/01 al 2022/07/01 únicamente debo pedir del 2021/01/01 al 2021/12/31.
# Manejo de errores de red y reconexiones.
# Visualización de parámetros técnicos.
# Links útiles
# [API de valores de finanzas] (https://polygon.io/docs/stocks/getting-started).
# [Libreria de base de datos] (https://docs.python.org/3/library/sqlite3.html).
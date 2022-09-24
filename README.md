Programa Final, Certificación Profesional Python
==============================

[![TravisCI](https://travis-ci.org/uber/Python-Sample-Application.svg?branch=master)](https://travis-ci.org/uber/Python-Sample-Application)
[![Coverage Status](https://coveralls.io/repos/uber/Python-Sample-Application/badge.png)](https://coveralls.io/r/uber/Python-Sample-Application)

https://developer.uber.com/

¿Cuál es el objetivo del programa?
-------------

El objetivo del programa es poder obtener datos de una base de datos de finanzas, mantenerlos en una base de datos propia y graficarlos temporalmente. La aplicación grafica los valores diarios junto con el volumen, las bandas Bollinger superior e inferior.
 
¿Cómo correr el programa?
---------------

1. Descargar `API_finanzas.py`, `tickers.db` y `requirements.txt` en una misma carpeta de su computadora.
2. Abrir el “Símbolo del sistema” y tipear `pip install -r requirements.txt` para instalar los paquetes necesarios.
3. Ejecutar desde la carpeta donde descargó los archivos, `python API_finanzas.py`


¿Cómo usarlo?
---------------
1. Al inicializar, se tendrá que elegir una opción, según lo que se quiera hacer:
     - 1- Actualización de datos
     - 2- Visualización de datos


```
 ******************************************************
        Te damos la Bienvenida. API de Finanzas
                Certificación Python ITBA
    ******************************************************
    MENU PRINCIPAL:
    1- Actualización de datos
    2- Visualización de datos

¿Cuál opción desea elegir?:
```

Si se ingresa `1`, se va a ingresar al menú de Actualización de datos.
Debe ingresar el nombre del Ticker a cargar en la base de datos junto al rango de fechas requerido, utilizando el formato `año-mes-día` . Si alguna fecha requerida ya se encuentra cargada en la base de datos, no la cargará nuevamente.

Ejemplo:
```
¿Cuál opción desea elegir?:1


ACTUALIZACIÓN DE DATOS.


Ingrese ticker a pedir y luego apriete <enter>.

Ticker:AAPL


Ingrese fecha de inicio [AAAA-MM-DD]:
 2021-02-03


Ingrese fecha de fin [AAAA-MM-DD]:
 2022-02-03

```

Desarrollo
--------------- 

Para desarrollar la aplicación se utilizó sqlite3 y se crea dos base de datos con la siguiente estructura: Tabla de datos (Nombre del ticker, fecha, volumen operado, valor medio, valor de apertura, valor de cierre, mayor valor, menor valor y timestamp), Tickers (Nombre del ticker, fecha de inicio de los datos, fecha de fin de los datos).

En la base de tabla de datos se guarda la información recibida de la API de finanzas y en la base de Tickers los requests recibidos del usuario.


Estructura del programa
---------------




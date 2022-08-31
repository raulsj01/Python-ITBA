#!/usr/bin/env python

import time
import sqlite3
import requests

#valor para loop
salir=2

#iniciamos la interfaz del usuario en loop
while salir != 0:
    print("""
    ******************************************************
        Te damos la Bienvenida. API de Finanzas
                Certificación Python ITBA
    ******************************************************
    MENU PRINCIPAL:
    1- Actualización de datos
    2- Visualización de datos
    """)

    option = input('¿Cuál opción desea elegir?:')
    print("\n ")
    if option == "1":
    #inicio opcion 1
            print("ACTUALIZACIÓN DE DATOS.")
            print("\n ")
            print("Ingrese ticker a pedir y luego apriete <enter>.\n ")
            ticker = input('Ticker:')
            print("\n ")
            f_inicial = input('Ingrese fecha de inicio [AAAA-MM-DD]:\n ')
            print("\n ")
            f_final = input('Ingrese fecha de fin [AAAA-MM-DD]:\n ')
            print("\n ")
            print("Pidiendo datos ...\n ")

            #Creamos la API key con los valores propuestos
            pedido= ("https://api.polygon.io/v2/aggs/ticker/{t}/range/1/day/{fi}/{ff}?adjusted=true&sort=asc&limit=120&apiKey=Hl28_xet0aqM7JlJ8rMwSoa7rVqhC_uo"
            .format(t=ticker,
                    fi=f_inicial,
                    ff=f_final,
                    )
                    )

            #realizamos el pedido a la pagina de la API
            json_file = requests.get(pedido)

            #mostramos los resultados
            print("Contendio en JSON:\n", json_file.json())

            print(json_file.text)

            json_obj = json_file.json() # Parseo a Diccionario de Python

            ticker = json_obj["ticker"]
            value = json_obj["results"]

            print(ticker)
            print(value)

            print(f"Ticker: {ticker} - {value[0]['v']}")
        

            # Creamos una conexión con la base de datos
            con = sqlite3.connect('tickers.db')
            # Creamos el cursor para interactuar con los datos
            cursor = con.cursor()


            for k in range(int(json_obj["queryCount"])):
                    cursor.execute( '''INSERT INTO datos (
                    nombre,
                    fechas,
                    close,
                    high,
                    low,
                    n,
                    open,
                    timestamp,
                    vol,
                    val_w                )
                    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (ticker, f_inicial, value[k]['c'], value[k]['h'], value[k]['l'], value[k]['n'], value[k]['o'], value[k]['t'], value[k]['v'],value[k]['vw']))

                    con.commit()
            print(cursor.rowcount, "datos guardados correctamente.")
            # Cerramos la conexión
            con.close()

            #manejo de menu
            print("\n ")
            input1 = input('Si quiere salir entre 0, de lo contrario ingrese 1:')
            salir = int(input1)

    #inicio de la opcion 2
    else:
            print("""
 VISUALIZACIÓN DE DATOS:
      1- Resumen
      2- Gráfico de ticker
            """)

            option1 = input('¿Cuál opción desea elegir?:')
            if option1 == "1":
                #inicio opcion 1 - RESUMEN
                        # Creamos una conexión con la base de datos
                        con = sqlite3.connect('tickers.db')
                        # Creamos el cursor para interactuar con los datos
                        cursor = con.cursor()


                        # Pedimos parametros al SQL
                        res = cursor.execute(f'''
                            SELECT nombre, f_inicio, f_fin
                            FROM ticker
                            ORDER BY nombre DESC
                            ''')

                        #imprimimos los datos pedidos
                        print("Los tickers guardados en la base de datos son:\n ")
                        for row in res:
                            print(f'{row[0]} - {row[1]} <-> {row[2]}')
                            print(row[0],"-",row[1],"<->",row[2])

                        # Cerramos la conexión
                        con.close()

                        print("\n ")
                        input1 = input('Si quiere salir entre 0, de lo contrario ingrese 1:')
                        salir = int(input1)

            #inicio de la opcion 2 - GRAFICO
            else:
                    print("Gráfico de ticker - No lo hice aún")

                    print("\n ")
                    input1 = input('Si quiere salir ingrese 0, de lo contrario ingrese 1:')
                    salir = int(input1)

import sqlite3

miConexion = sqlite3.connect("Test_database") #Si no existe la base de datos la crea
miCursor = miConexion.cursor() 

""" ----------------- DDL ----------------------"""

# miCursor.execute("""
#     CREATE TABLE IF NOT EXISTS PRODUCTOS(
#         codigo_articulo INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre_articulo VARCHAR(50),
#         precio INTEGER,
#         seccion VARCHAR(20)
#         );
#     """)

""" ------------------ DML ---------------------"""

""" Insert single element """

# miCursor.execute("""
#     INSERT INTO PRODUCTOS VALUES(
#         NULL,
#         'ARTICULO 1',
#         50,
#         'SECCION 1'
#         );
#     """) 

""" Insert many elements """

# variosProductos = [ #Create a list of tuples
#     ('CAMISETA', 10, 'DEPORTES'),
#     ('JARRON', 90, 'CERAMICA'),
#     ('CAMION', 20, 'JUGUETERIA')
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",variosProductos)


""" Select elements """
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'JUGUETERIA'") #SQL is case sensitive
productos=miCursor.fetchall() #Stores in a variable the result of the query in tuples
print(productos) #Prints on console.

""" Update elements """
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE nombre_articulo = 'CAMISETA'")

""" Delete elements """
miCursor.execute("DELETE FROM PRODUCTOS WHERE codigo_articulo = 1")
miConexion.commit()


miConexion.close()


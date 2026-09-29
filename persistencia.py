import json

#----------------- Cargar Productos JSON------------------------------------------------------------------------------------------------------

# Carga los productos almacenados en el archivo JSON.
def cargar_productos():
    archivo = open('productos.json', 'r')

    productos = json.load(archivo)

    archivo.close()

    return productos

#----------------- Guardar Productos JSON------------------------------------------------------------------------------------------------------

# Guarda la lista de productos en el archivo JSON.
def guardar_productos(productos):
    archivo = open('productos.json', 'w')

    json.dump(productos, archivo, indent=4)

    archivo.close()
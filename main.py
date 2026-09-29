import json

#Importo las funciones principales para el producto
from productos import (
    agregar_producto,
    listar_productos,
    buscar_producto,
    actualizar_stock,
    calcular_valor_inventario,
    eliminar_producto
)

#Importo las funciones para el guardado de los productos en JSON
from persistencia import cargar_productos, guardar_productos

# Muestra las opciones disponibles del programa.
def mostrar_menu():
    print('===== SPORT-IT =====\n')
    print('1. Alta de producto')
    print('2. Listado de productos')
    print('3. Buscar producto por ID')
    print('4. Actualizar stock')
    print('5. Calcular valor del inventario')
    print('6. Eliminar producto')
    print('7. Salir')

# Controla el funcionamiento principal del programa.
def main():
    productos = cargar_productos()

    while True:
        mostrar_menu()
        opcion = input('Seleccione una opcion: ')

        match opcion:
            case '1':
                agregar_producto(productos)
                guardar_productos(productos)

            case '2':
                listar_productos(productos)

            case '3':
                buscar_producto(productos)

            case '4':
                actualizar_stock(productos)
                guardar_productos(productos)

            case '5':
                calcular_valor_inventario(productos)

            case '6':
                eliminar_producto(productos)
                guardar_productos(productos)

            case '7':
                break

            case _:
                print('Ingrese una opcion valida!!')


if __name__ == '__main__':
    main()
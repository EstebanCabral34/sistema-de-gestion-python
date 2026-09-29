import json

productos = []

def agregar_producto(productos):
    while True:
        id = input('Ingrese el id del producto = ')

        if id.isdigit() == False:
            print('Tipo de dato incorrecto, solo pueden ser numeros enteros')
            continue
        else:
            id = int(id)

        id_existe = False

        for producto in productos:
            if producto['id'] == id:
                id_existe = True
                break

        if id_existe:
            print('Ese ID ya existe.')
            continue

        nombre = input('Ingrese el nombre del producto = ')

        categoria = input('Ingrese la categoria del producto = ')

        precio = input('Ingrese el precio del producto = ')

        precio = precio.replace(',', '.')

        if precio.count('.') > 1:
            print('Precio invalido')
            continue

        partes = precio.split('.')

        if not all(parte.isdigit() for parte in partes):
            print('Precio invalido')
            continue
        else:
            precio = float(precio)

        stock = input('Ingrese el stock del producto = ')

        if stock.isdigit() == False:
            print('Tipo de dato incorrecto, solo pueden ser numeros enteros')
            continue
        else:
            stock = int(stock)

        producto = {
            'id': id,
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'stock': stock
        }

        productos.append(producto)

        print('✅ ¡Producto agregado con éxito!')

        break

    return productos

def listar_productos(productos):
    if not productos:
        print('No hay productos cargados!!!')
    else:
        print('===== LISTADO DE PRODUCTOS =====')

        for indice in productos:
            for clave, valor in indice.items():
                print(f'{clave}: {valor}')

def buscar_producto(productos):

    while True:
            id = input('Ingrese el id del producto = ')
    
            if(id.isdigit() == False):
                print('Tipo de dato incorrecto solo pueden ser numeros enteros')
                continue
            else:
                id = int(id)
                break

    for indice in productos:
        if (id == indice.get('id')):
            print('Producto encontrado!')
            return indice
    
    
    print('Producto no encontrado.')
    return None

def actualizar_stock(productos):

    indice = buscar_producto(productos)

    if(indice != None):
        nuevoStock = input('Ingrese el nuevo stock: ')
        if(nuevoStock.isdigit() == False):
            print('Tipo de dato incorrecto solo pueden ser numeros enteros')
        else:
            nuevoStock = int(nuevoStock)
            indice['stock'] = nuevoStock
            print('Stock actualizado correctamente.')

def calcular_valor_inventario(productos):
    total = 0
    
    for indice in productos:
        stockInventario = indice.get('stock')
        precioInventario = indice.get('precio')
        total += precioInventario * stockInventario

    print(f'El valor del inventario es de {total}')
    return total

def eliminar_producto(productos):
    indice = buscar_producto(productos)

    if(indice != None):
        productos.remove(indice)
        print('Producto eliminado con exito!')
    else:
        print('El producto no existe.')

def cargar_productos():
    archivo = open('productos.json', 'r')

    productos = json.load(archivo)

    archivo.close()

    return productos

def guardar_productos(productos):
    archivo = open('productos.json', 'w')

    json.dump(productos, archivo)

    archivo.close()

def mostrar_menu():
    print('===== SPORT-IT =====\n')
    print('1. Alta de producto')
    print('2. Listado de productos')
    print('3. Buscar producto por ID')
    print('4. Actualizar stock')
    print('5. Calcular valor del inventario')
    print('6. Eliminar producto')
    print('7. Salir')

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
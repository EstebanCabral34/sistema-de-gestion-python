#----------------- Agregar Productos ------------------------------------------------------------------------------------------------------

# Registra un nuevo producto y valida los datos ingresados.
def agregar_producto(productos):
    while True:
        id_producto = input('Ingrese el id del producto = ')

        if id_producto.isdigit() == False:
            print('Tipo de dato incorrecto, solo pueden ser numeros enteros')
            continue
        else:
            id_producto = int(id_producto)

        # Verifica que el ID no esté utilizado.
        id_existe = False

        for producto in productos:
            if producto['id'] == id_producto:
                id_existe = True
                break

        if id_existe:
            print('Ese ID ya existe.')
            continue

        nombre = input('Ingrese el nombre del producto = ')

        categoria = input('Ingrese la categoria del producto = ')

        precio = input('Ingrese el precio del producto = ')
        precio = precio.replace(',', '.')

        # Valida que el precio tenga un formato numérico correcto.
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

        # Crea el diccionario que representa al producto.
        producto = {
            'id': id_producto,
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'stock': stock
        }

        productos.append(producto)

        print('Producto agregado con exito!')

        break

    return productos

#----------------- Listar Productos ------------------------------------------------------------------------------------------------------

# Muestra todos los productos registrados.
def listar_productos(productos):
    if not productos:
        print('No hay productos cargados!!!')
    else:
        print('===== LISTADO DE PRODUCTOS =====')

        for producto in productos:
            for clave, valor in producto.items():
                print(f'{clave}: {valor}')

#----------------- Buscar Productos ------------------------------------------------------------------------------------------------------

# Busca un producto utilizando su ID.
def buscar_producto(productos):

    while True:
        id_producto = input('Ingrese el id del producto = ')

        if id_producto.isdigit() == False:
            print('Tipo de dato incorrecto, solo pueden ser numeros enteros')
            continue
        else:
            id_producto = int(id_producto)
            break

    for producto in productos:
        if id_producto == producto.get('id'):
            print('Producto encontrado!')
            return producto

    print('Producto no encontrado.')
    return None

#----------------- Actualizar Stock ------------------------------------------------------------------------------------------------------

# Busca un producto y permite modificar su stock.
def actualizar_stock(productos):

    producto = buscar_producto(productos)

    if producto != None:
        while True:
            nuevo_stock = input('Ingrese el nuevo stock: ')

            if nuevo_stock.isdigit() == False:
                print('Tipo de dato incorrecto, solo pueden ser numeros enteros')
                continue

            nuevo_stock = int(nuevo_stock)
            producto['stock'] = nuevo_stock

            print('Stock actualizado correctamente.')
            break

#----------------- Calcular valor de Inventario ------------------------------------------------------------------------------------------

# Calcula el valor total del inventario.
def calcular_valor_inventario(productos):
    total = 0

    for producto in productos:
        stock = producto.get('stock')
        precio = producto.get('precio')

        total += precio * stock

    print(f'El valor del inventario es de {total}')

    return total

#----------------- Eliminar Productos ------------------------------------------------------------------------------------------------------

# Busca y elimina un producto de la lista.
def eliminar_producto(productos):
    producto = buscar_producto(productos)

    if producto != None:
        productos.remove(producto)
        print('Producto eliminado con exito!')
    else:
        print('El producto no existe.')
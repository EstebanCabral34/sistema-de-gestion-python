productos = []

def agregar_producto(productos):
    while True:
        id = input('Ingrese el id del producto = ')

        if(id.isdigit() == False):
            print('Tipo de dato incorrecto solo pueden ser numeros enteros')
            continue
        else:
            id = int(id)

        nombre = input('Ingrese el nombre del producto = ')

        categoria = input('Ingrese la categoria del producto = ')

        precio = input('Ingrese el precio del producto = ')

        if(precio.isdecimal() == False):
            print('Tipo de dato incorrecto solo pueden ser numeros decimales')
            continue
        else:
            precio = precio.replace(',', '.')
            precio = float(precio)

        stock = input('Ingrese el stock del producto = ')

        if(stock.isdigit() == False):
            print('Tipo de dato incorrecto solo pueden ser numeros enteros')
            continue
        else:
            stock = int(stock)

        producto = {
            'id': id,
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'stock': stock}

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
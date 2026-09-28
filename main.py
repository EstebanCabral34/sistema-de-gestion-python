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
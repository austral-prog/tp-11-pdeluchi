def read_file_to_dict(filename):
    ventas_dict = {}

    with open(filename, 'r') as f:
        linea = f.readline().strip()
        ventas = linea.split(';')

        for venta in ventas:
            if venta:
                producto, valor = venta.split(':')
                valor = float(valor)

                if producto not in ventas_dict:
                    ventas_dict[producto] = []
                ventas_dict[producto].append(valor)

    return ventas_dict


def process_dict(data):
    for producto in sorted(data.keys()):
        lista_ventas = data[producto]
        total = sum(lista_ventas)
        promedio = total / len(lista_ventas)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

print("----EJERCICIO 9-----")
print("sistema tienda")
confirmacion = input("Registrar nueva venta 'si' o 'no': ")

if confirmacion == 'si':
    cantidad = int(input("Cantidad de productos comprados: "))
    contador = 1
    suma = 0
    
    while contador <= cantidad:
        producto = float(input("Ingrese el precio del producto {}: ".format(contador)))
        suma += producto
        contador += 1
        
    print("Valor compra:", suma)
    iva = suma * 0.16
    print("Valor de IVA:", iva)
    total = suma + iva
    print("Valor total:", total)
else:
    print("Error")

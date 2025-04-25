# sistema_validacion_productos.py
# Programa que calcula el costo total de una compra con descuento, aplicando validaciones.

# ------------------------
# PASOS A SEGUIR
# ------------------------

# Paso 1: Análisis y planificación del problema
# - Objetivo: Calcular el costo total de una compra aplicando un posible descuento.
# - Datos requeridos: nombre del producto, precio unitario, cantidad, porcentaje de descuento.
# - Validaciones necesarias:
#     * Precio debe ser un número positivo.
#     * Cantidad debe ser un entero positivo.
#     * Descuento debe estar entre 0% y 100%.

# Paso 2: Entrada y validación de datos
# - Solicitar al usuario los cuatro datos necesarios.
# - Validar que los datos sean del tipo correcto y cumplan con los rangos permitidos.

# Paso 3: Desarrollo de la lógica del programa
# - Calcular el costo sin descuento: precio * cantidad.
# - Calcular el descuento: (descuento/100) * costo.
# - Calcular el total a pagar: costo - descuento.

# Paso 4: Generación y formato de resultados
# - Mostrar en pantalla:
#     * Nombre del producto.
#     * Precio unitario formateado.
#     * Cantidad.
#     * Porcentaje de descuento aplicado.
#     * Costo total formateado con dos decimales.

# Paso 5: Pruebas y revisión
# - Probar con diferentes escenarios:
#     * Sin descuento (0%).
#     * Descuento completo (100%).
#     * Entradas inválidas (texto, negativos, fuera de rango).
#     * Valores límite (cantidad muy alta, precio alto).

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Pedimos los datos al usuario
print("-" * 30)
print(" SISTEMA DE CÁLCULO DE COMPRAS")
print("-" * 30)


# Pedimos el nombre del producto
nombreProducto = input("\nIngrese el nombre del producto: ")
while nombreProducto.strip() == "":
    print("Error: Debe ingresar un nombre de producto.")
    nombreProducto = input("Ingrese el nombre del producto: ")

# Pedimos y validamos el precio unitario
precioUnitario = 0
while precioUnitario <= 0:
    try:
        precioUnitario = float(input("Ingrese el precio unitario: "))
        if precioUnitario <= 0:
            print("Error: El precio debe ser mayor que cero.")
    except ValueError:
        print("Error: Ingrese un número válido.")
        
# Pedimos y validamos la cantidad
cantidad = 0



#while es un ciclo que se repite mientras la condicion sea verdad
while cantidad <= 0:
    
    try:#try sirve para capturar errores
        
        cantidad = int(input("Ingrese la cantidad: "))#input solicita informacion al usuario 
        if cantidad <= 0:
            print("Error: La cantidad debe ser un número entero positivo.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

# Pedimos y validamos el porcentaje de descuento
descuento = -1
while descuento < 0 or descuento > 100:
    try:
        descuento = float(input("Ingrese el porcentaje de descuento (0-100): "))
        if descuento < 0 or descuento > 100:
            print("Error: El descuento debe estar entre 0 y 100.")
    except ValueError:# except sirve para capturar errores
        print("Error: Ingrese un número válido.")

# Calculamos el costo
SinDescuento = precioUnitario * cantidad
MontoDescuento = (descuento / 100) * SinDescuento
totalPagar = SinDescuento - MontoDescuento

# print para Mostrar los resultados
print("\nRESUMEN DE LA COMPRA")
print("-" * 30) # se utiliza para crear una linea de 30 guines ------
print(f"Producto: {nombreProducto}")
print(f"Precio unitario: ${precioUnitario:}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${SinDescuento:}")
print(f"Descuento ({descuento}%): ${MontoDescuento:}")
print(f"TOTAL A PAGAR: ${totalPagar:}")

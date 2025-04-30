"""
Sistema de Gestión de Calificaciones
Este programa permite:
1. Determinar si un estudiante aprobó o reprobó según su calificación
2. Calcular el promedio de una lista de calificaciones
3. Contar cuántas calificaciones son mayores que un valor específico
4. Verificar y contar la presencia de calificaciones específicas
"""

def solicitar_calificacion_individual():
    """Solicita y valida una calificación individual del usuario"""
    while True:
        entrada = input("Ingrese la calificación (0-100): ")
        # Intentar convertir a número
        if entrada.replace('.', '', 1).isdigit():
            calificacion = float(entrada)
            # Validación de rango
            if 0 <= calificacion <= 100:
                return calificacion
            else:
                print("Error La calificación debe estar entre 0 y 100.")
        else:
            print("Error Ingrese un valor numérico válido.")

def evaluar_aprobacion(calificacion):
    """Evalúa si una calificación corresponde a aprobado o reprobado"""
    if calificacion >= 70:
        return True
    else:
        return False

def mostrar_resultado_aprobacion(calificacion, aprobado):
    """Muestra un mensaje indicando si el estudiante aprobó o reprobó"""
    if aprobado:
        print(f"La calificación {calificacion} indica que el estudiante ha APROBADO.")
    else:
        print(f"La calificación {calificacion} indica que el estudiante ha REPROBADO.")

def determinar_estado_aprobacion():
    """Determina si un estudiante aprobó o reprobó según su calificación"""
    # Solicitar calificación
    calificacion = solicitar_calificacion_individual()
    
    # Evaluar aprobación
    aprobado = evaluar_aprobacion(calificacion)
    
    # Mostrar resultado
    mostrar_resultado_aprobacion(calificacion, aprobado)

def obtener_lista_calificaciones():
    """Solicita y valida una lista de calificaciones del usuario"""
    while True:
        entrada = input("Ingrese lista de calificaciones separadas por comas: ")
        calificaciones = []
        valores_validos = True
        
        # Procesar cada elemento en la entrada
        elementos = entrada.split(",")
        for elemento in elementos:
            elemento = elemento.strip()
            # Verificar si es un número válido
            if elemento.replace('.', '', 1).isdigit():
                cal = float(elemento)
                # Validar rango
                if 0 <= cal <= 100:
                    calificaciones.append(cal)
                else:
                    print(f"Error La calificación {cal} está fuera del rango válido (0-100).")
                    valores_validos = False
                    break
            else:
                print(f"Error: '{elemento}' no es un valor numérico válido.")
                valores_validos = False
                break
        
        if valores_validos and len(calificaciones) > 0:
            return calificaciones
        elif valores_validos and len(calificaciones) == 0:
            print("Error Debe ingresar al menos una calificación.")

def calcular_suma(calificaciones):
    """Calcula la suma de las calificaciones en la lista"""
    suma = 0
    for cal in calificaciones:
        suma += cal
    return suma

def calcular_promedio():
    """Calcula el promedio de una lista de calificaciones"""
    # Obtener lista de calificaciones
    calificaciones = obtener_lista_calificaciones()
    
    # Calcular promedio usando función auxiliar
    suma = calcular_suma(calificaciones)
    promedio = suma / len(calificaciones)
    
    # Mostrar resultado
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
    
    return calificaciones, promedio

def solicitar_valor_comparacion():
    """Solicita y valida un valor para comparar con las calificaciones"""
    while True:
        entrada = input("Ingrese el valor para comparar: ")
        if entrada.replace('.', '', 1).isdigit():
            valor = float(entrada)
            if 0 <= valor <= 100:
                return valor
            else:
                print("Error El valor debe estar entre 0 y 100.")
        else:
            print("Error Ingrese un valor numérico válido.")

def realizar_conteo_mayores(calificaciones, valor):
    """Cuenta cuántas calificaciones son mayores que un valor específico"""
    contador = 0
    i = 0
    while i < len(calificaciones):
        if calificaciones[i] > valor:
            contador += 1
        i += 1
    return contador

def mostrar_resultado_conteo(contador, valor):
    """Muestra el resultado del conteo de calificaciones mayores"""
    print(f"Hay {contador} calificaciones mayores que {valor}.")

def contar_calificaciones_mayores(calificaciones):
    """Coordina el proceso de contar calificaciones mayores que un valor"""
    # Solicitar valor de comparación
    valor = solicitar_valor_comparacion()
    
    # Realizar conteo
    contador = realizar_conteo_mayores(calificaciones, valor)
    
    # Mostrar resultado
    mostrar_resultado_conteo(contador, valor)

def solicitar_calificacion_buscar():
    """Solicita y valida una calificación específica a buscar"""
    while True:
        entrada = input("Ingrese la calificación específica a buscar: ")
        if entrada.replace('.', '', 1).isdigit():
            cal_especifica = float(entrada)
            if 0 <= cal_especifica <= 100:
                return cal_especifica
            else:
                print("Error: La calificación debe estar entre 0 y 100.")
        else:
            print("Error: Ingrese un valor numérico válido.")

def contar_apariciones(calificaciones, cal_especifica):
    """Cuenta cuántas veces aparece una calificación específica en la lista"""
    contador = 0
    for cal in calificaciones:
        # Si es una calificación muy baja, continuamos sin contar
        if cal < 50 and cal != cal_especifica:
            continue
            
        # Si encontramos exactamente la calificación buscada
        if abs(cal - cal_especifica) < 0.001:  # Comparación de punto flotante
            contador += 1
    return contador

def mostrar_resultado_busqueda(cal_especifica, contador):
    """Muestra el resultado de la búsqueda de una calificación específica"""
    if contador > 0:
        print(f"La calificación {cal_especifica} aparece {contador} veces en la lista.")
    else:
        print(f"La calificación {cal_especifica} no aparece en la lista.")

def verificar_calificacion_especifica(calificaciones):
    """Verifica y cuenta la presencia de una calificación específica"""
    # Solicitar calificación a buscar
    cal_especifica = solicitar_calificacion_buscar()
    
    # Contar apariciones
    contador = contar_apariciones(calificaciones, cal_especifica)
    
    # Mostrar resultado
    mostrar_resultado_busqueda(cal_especifica, contador)

def mostrar_menu():
    """Muestra el menú principal del programa"""
    print("\n--- SISTEMA DE GESTIÓN DE CALIFICACIONES ---\n")
    print("1. Determinar estado de aprobación")
    print("2. Calcular promedio de calificaciones")
    print("3. Contar calificaciones mayores que un valor")
    print("4. Verificar presencia de calificación específica")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

def verificar_lista_calificaciones(calificaciones):
    """Verifica si existe una lista de calificaciones y solicita crearla si no existe"""
    if not calificaciones:
        print("Primero debe calcular el promedio para tener una lista de calificaciones.")
        return obtener_lista_calificaciones()
    return calificaciones

def procesar_opcion(opcion, calificaciones, promedio):
    """Procesa la opción seleccionada por el usuario"""
    if opcion == "1":
        determinar_estado_aprobacion()
        return calificaciones, promedio
    elif opcion == "2":
        calificaciones = obtener_lista_calificaciones()
        suma = calcular_suma(calificaciones)
        promedio = suma / len(calificaciones)
        print(f"El promedio de las calificaciones es: {promedio:.2f}")
        return calificaciones, promedio
    elif opcion == "3":
        calificaciones = verificar_lista_calificaciones(calificaciones)
        contar_calificaciones_mayores(calificaciones)
        return calificaciones, promedio
    elif opcion == "4":
        calificaciones = verificar_lista_calificaciones(calificaciones)
        verificar_calificacion_especifica(calificaciones)
        return calificaciones, promedio
    elif opcion == "5":
        print("¡Gracias por usar el Sistema de Gestión de Calificaciones!")
        return None, None
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        return calificaciones, promedio

def main():
    """Función principal que ejecuta el programa"""
    calificaciones = []
    promedio = 0
    
    while True:
        opcion = mostrar_menu()
        calificaciones, promedio = procesar_opcion(opcion, calificaciones, promedio)
        
        if opcion == "5":
            break

if __name__ == "__main__":
    main()
# Definición de la función que analiza una lista de números
def analizar_lista(lista):
    # Verifica si la lista está vacía
    if not lista:  # Si no hay elementos en la lista
        return {  # Retorna un diccionario con valores por defecto
            'suma': 0,           # Suma total = 0
            'mayor': None,        # No hay valor mayor
            'menor': None,        # No hay valor menor
            'promedio': 0         # Promedio = 0
        }
    
    # Calcula la suma de todos los elementos de la lista
    suma = sum(lista)
    
    # Obtiene el número más grande de la lista
    mayor = max(lista)
    
    # Obtiene el número más pequeño de la lista
    menor = min(lista)
    
    # Calcula el promedio (suma / cantidad de elementos) y redondea a 2 decimales
    promedio = round(suma / len(lista), 2)
    
    # Retorna un diccionario con los resultados
    return {
        'suma': suma,        # Suma total de los números
        'mayor': mayor,      # Número más grande
        'menor': menor,      # Número más pequeño
        'promedio': promedio # Promedio redondeado
    }

# Función para que el usuario ingrese los números
def ingresar_lista():
    # Solicita al usuario ingresar números separados por comas
    entrada = input("Ingresa los números separados por comas: ")
    
    # Convierte la entrada en una lista de números flotantes
    numeros = [float(num.strip()) for num in entrada.split(',') if num.strip()]
    
    # Retorna la lista de números
    return numeros

# Define una función para mostrar resultados formateados
# Recibe un diccionario con los resultados y no retorna nada (None)
def mostrar_resultado(resultado: dict[str, float]) -> None:
    # Imprime un encabezado para la sección de resultados
    print("\nResultado del análisis:")
    
    # Muestra la suma total con formato legible
    print(f"Suma total: {resultado['suma']}")
    
    # Muestra el valor máximo encontrado
    print(f"Valor máximo: {resultado['mayor']}")
    
    # Muestra el valor mínimo encontrado
    print(f"Valor mínimo: {resultado['menor']}")
    
    # Muestra el promedio calculado
    print(f"Promedio: {resultado['promedio']}")


# No recibe parámetros y no retorna nada (None)
def main() -> None:
    # Muestra el título de la aplicación
    print("Análisis de listas numéricas\n")
    
    try:
        #Obtiene la lista de números del usuario
        numeros = ingresar_lista()
        
        #Procesa la lista para obtener estadísticas
        resultado = analizar_lista(numeros)
        
        # Muestra los resultados formateados
        mostrar_resultado(resultado)
        
    #Captura errores específicos de valor
    except ValueError as error:
        # Muestra mensaje de error formateado
        print(f"\nError: {error}")
        
    # Captura cualquier otro error inesperado
    except Exception as error:
        # Muestra mensaje genérico de error
        print(f"\nOcurrió un error inesperado: {error}")


if __name__ == "__main__":
    # Ejecuta la función principal
    main()

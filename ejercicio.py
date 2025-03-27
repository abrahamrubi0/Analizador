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

# Ejemplo de uso
if __name__ == "__main__":
    numeros = ingresar_lista()
    resultado = analizar_lista(numeros)
    print("\nResultado del análisis:")
    print(resultado)

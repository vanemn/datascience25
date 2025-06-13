# 1.4 Equipo 4: Inventario de Recursos Urbanos
#  Construya una clase ResourceInventory para gestionar recursos urbanos (e.g., bancos,#  farolas). 
#  La clase debe incluir atributos para el ID del inventario (cadena) y una lista privada de recursos (cadenas). 
#  Implemente métodos add_resource(item) para agregar un recurso y
#  resource_frequency() para contar la frecuencia de un recurso específico.
#  Desarrolle una función resource_priority(count) que calcule una prioridad usando  math.log().
#  Acepte el ID y recursos vía input(), imprima la lista y la prioridad, y
#  estandarice los recursos con replace().


import math  

class ResourceInventory:  
    def __init__(self, inventory_id):  
        """Inicializa el inventario con un ID y una lista vacía de recursos."""  
        self.inventory_id = inventory_id  
        self._resources = []  # Lista privada de recursos  

    def add_resource(self, item):  
        """Agrega un recurso a la lista estandarizando su formato."""  
        item = item.replace("-", " ").strip().lower()  
        self._resources.append(item)  

    def resource_frequency(self, item):  
        """Cuenta la frecuencia de un recurso específico."""  
        item = item.lower()  
        return self._resources.count(item)  

    def resource_priority(self, count):  
        """Calcula la prioridad del recurso usando logaritmo."""  
        return math.log(count + 1) if count > 0 else 0  # Evita log(0)  

# Bloque principal para recibir entrada y procesar recursos
def main():  
    inventory_id = input("Ingrese el ID del inventario: ")  
    resources_input = input("Ingrese los recursos urbanos separados por comas: ")  

    # Crear instancia de ResourceInventory
    inventory = ResourceInventory(inventory_id)  

    # Procesar cada recurso y agregarlo a la lista  
    resources_list = resources_input.split(",")  
    for resource in resources_list:  
        inventory.add_resource(resource)  

    # Mostrar resultados
    print(f"\nInventario ID: {inventory.inventory_id}")  
    print(f"Lista de recursos urbanos: {inventory._resources}")  

    # Solicitar un recurso para verificar frecuencia y prioridad  
    resource_to_check = input("\nIngrese un recurso para verificar su frecuencia y prioridad: ")  
    freq = inventory.resource_frequency(resource_to_check)  
    priority = inventory.resource_priority(freq)  

    print(f"\nFrecuencia de '{resource_to_check}': {freq}")  
    print(f"Prioridad calculada: {priority:.2f}")  # Redondeo a 2 decimales  

# Ejecutar la función principal fuera de la clase
if __name__ == "__main__":  
    main()
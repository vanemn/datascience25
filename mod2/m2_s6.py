
#1. Crea la clase Libro con los atributos privados _titulo, _autor y _isbn (1 punto).
class Libro:
    #2. Define un constructor para Libro que inicialice estos atributos al momento de crear un objeto (1 punto). 
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
    #3. Implementa métodos get_titulo(), get_autor() y get_isbn() para obtener el valor de cada atributo desde fuera de la clase (2 puntos)
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_isbn(self):
        return self._isbn
    #4. Crea un método descripcion() en la clase Libro  que retorne una cadena con los detalles del libro en el formato “Título: [titulo], Autor: [autor], ISBN: [isbn]” (2 puntos). 
    def descripcion(self):
        return f"Titulo: {self._titulo}, Autor: {self._autor}, ISBN: {self._isbn}"
    
#5. Crea una clase Biblioteca que permita gestionar una lista de libros. Define un método agregar_libro() para añadir un libro a la biblioteca (1 punto). 
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    #6. Define un método mostrar_libro() en Biblioteca que recorra la lista de libros e imprima la descripción de cada libro (2 puntos). 
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.descripcion())
#7. Instancia la clase Biblioteca, crea al menos dos libros y añádelos a la biblioteca. Luego, muestra los detalles de los libros almacenados (1 punto). 
# Instancir
biblioteca = Biblioteca()

# Creamos algunos libros y los agregar  a la biblioteca
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-654321")
libro2 = Libro("El señor de los anillos", "J.R.R. Tolkien", "978-765432")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Mostramos los detalles de los libros almacenados
biblioteca.mostrar_libros()
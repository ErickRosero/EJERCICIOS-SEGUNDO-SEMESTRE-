class FileHandler:
    """
    Esta clase maneja la apertura y cierre de archivos.
    """

    def __init__(self, filename):
        """
        Constructor que inicializa el atributo filename y abre el archivo para escritura.
        """
        self.filename = filename
        # Abre el archivo en modo de escritura
        try:
            self.file = open(self.filename, 'w')
            print(f"Archivo '{self.filename}' abierto para escritura.")
        except Exception as e:
            print(f"No se pudo abrir el archivo '{self.filename}': {e}")

    def write(self, content):
        """
        Escribe contenido en el archivo.
        """
        if hasattr(self, 'file'):
            self.file.write(content)
            print(f"Escrito en el archivo '{self.filename}'.")
        else:
            print(f"El archivo '{self.filename}' no está abierto.")

    def __del__(self):
        """
        Destructor que cierra el archivo cuando el objeto es destruido.
        """
        if hasattr(self, 'file'):
            self.file.close()
            print(f"Archivo '{self.filename}' cerrado.")


class DataProcessor:
    """
    Esta clase procesa datos y realiza operaciones básicas.
    """

    def __init__(self, data):
        """
        Constructor que inicializa el atributo data.
        """
        self.data = data
        print(f"Datos inicializados: {self.data}")

    def process(self):
        """
        Procesa los datos (en este caso, simplemente los convierte a mayúsculas).
        """
        self.data = self.data.upper()
        print(f"Datos procesados: {self.data}")

    def __del__(self):
        """
        Destructor que limpia cualquier recurso al finalizar el uso.
        """
        print(f"Objeto DataProcessor con datos '{self.data}' ha sido destruido.")


# Ejemplo de uso de las clases

if __name__ == "__main__":
    # Crear un objeto de FileHandler
    file_handler = FileHandler('example.txt')
    file_handler.write("Este es un ejemplo de contenido.\n")

    # Crear un objeto de DataProcessor
    data_processor = DataProcessor("datos de prueba")
    data_processor.process()

    # Eliminar los objetos
    del file_handler
    del data_processor

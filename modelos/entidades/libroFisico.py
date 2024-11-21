from modelos.entidades.libro import Libro

class LibroFisico(Libro):

    def __init__(self, ISBN: int, titulo: str, autor: str, editorial: str, precio: float, stock: int, 
                 alto:float, ancho:float, grosor:float, tapaDura:bool, peso: float):
        super().__init__(ISBN, titulo, autor, editorial, precio, stock)
        if not isinstance(alto, (int,float)) or alto <= 0:
            raise ValueError('El alto debe ser un número positivo')
        if not isinstance(ancho, (int,float)) or ancho <= 0:
            raise ValueError('El ancho debe ser un número positivo')
        if not isinstance(grosor, (int,float)) or grosor <= 0:
            raise ValueError('El grosor debe ser un número positivo')
        if not isinstance(tapaDura, bool):
            raise ValueError('El valor de tapaDura debe ser un booleano')
        if not isinstance(peso, (int,float)) or peso <= 0:
            raise ValueError('El peso debe ser un número positivo')
        self.__alto = alto
        self.__ancho = ancho
        self.__grosor = grosor
        self.__tapaDura = tapaDura
        self.__peso = peso

    def obtenerAlto(self):
        return self.__alto
    
    def obtenerAncho(self):
        return self.__ancho
    
    def obtenerGrosor(self):
        return self.__grosor
    
    def obtenerTapaDura(self):
        return self.__tapaDura
    
    def obtenerPeso(self):
        return self.__peso
    
    def establecerAlto(self, alto: float):
        if not isinstance(alto, (int,float)) or alto <= 0:
            raise ValueError('El alto debe ser un número positivo')
        self.__alto = alto

    def establecerAncho(self, ancho: float):
        if not isinstance(ancho, (int,float)) or ancho <= 0:
            raise ValueError('El ancho debe ser un número positivo')        
        self.__ancho = ancho

    def establecerGrosor(self, grosor: float):
        if not isinstance(grosor, (int,float)) or grosor <= 0:
            raise ValueError('El grosor debe ser un número positivo')
        self.__grosor = grosor

    def establecerTapaDura(self, tapaDura: bool):
        if not isinstance(tapaDura, bool):
            raise ValueError('El valor de tapaDura debe ser un booleano')
        self.__tapaDura = tapaDura

    def establecerPeso(self, peso: float):
        if not isinstance(peso, (int,float)) or peso <= 0:
            raise ValueError('El peso debe ser un número positivo')
        self.__peso = peso

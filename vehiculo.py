"""
Módulo vehiculo.
cambio
Define la clase base Vehiculo.
"""

class Vehiculo:
    """
    Clase base que representa un vehículo genérico.

    :param marca: Marca del vehículo.
    :type marca: str
    :param modelo: Modelo del vehículo.
    :type modelo: str
    :param anio: Año de fabricación.
    :type anio: int
    """

    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self) -> str:
        """
        Devuelve una descripción básica del vehículo.

        :return: Descripción formateada del vehículo.
        :rtype: str
        """
        return f"{self.marca} {self.modelo} ({self.anio})"

    def arrancar(self) -> str:
        """
        Simula el arranque del vehículo.

        :return: Mensaje indicando que el vehículo ha arrancado.
        :rtype: str
        """
        return "El vehículo ha arrancado."
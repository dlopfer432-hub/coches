"""
Módulo coche.

Define la clase Coche que hereda de Vehiculo.
"""

from vehiculo import Vehiculo


class Coche(Vehiculo):
    """
    Representa un coche.

    :param marca: Marca del coche.
    :type marca: str
    :param modelo: Modelo del coche.
    :type modelo: str
    :param anio: Año de fabricación.
    :type anio: int
    :param puertas: Número de puertas.
    :type puertas: int
    """

    def __init__(self, marca: str, modelo: str, anio: int, puertas: int):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def descripcion(self) -> str:
        """
        Devuelve una descripción completa del coche.

        :return: Descripción detallada del coche.
        :rtype: str
        """
        return f"{super().descripcion()} - {self.puertas} puertas"

    def tocar_claxon(self) -> str:
        """
        Simula el sonido del claxon.

        :return: Sonido del claxon.
        :rtype: str
        """
        return "¡Beep beep!"
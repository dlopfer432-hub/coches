"""
Módulo moto.

Define la clase Moto que hereda de Vehiculo.
"""

from vehiculo import Vehiculo


class Moto(Vehiculo):
    """
    Representa una moto.

    :param marca: Marca de la moto.
    :type marca: str
    :param modelo: Modelo de la moto.
    :type modelo: str
    :param anio: Año de fabricación.
    :type anio: int
    :param cilindrada: Cilindrada en cc.
    :type cilindrada: int
    """

    def __init__(self, marca: str, modelo: str, anio: int, cilindrada: int):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

    def hacer_caballito(self) -> str:
        """
        Simula que la moto hace un caballito.

        :return: Mensaje indicando la acción.
        :rtype: str
        """
        return "La moto está haciendo un caballito."
"""
Módulo concesionario.

Gestiona un conjunto de vehículos.
"""

from typing import List
from vehiculo import Vehiculo


class Concesionario:
    """
    Representa a un concesionario de vehículos.

    :param nombre: Nombre del concesionario.
    :type nombre: str
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.vehiculos: List[Vehiculo] = []

    def agregar_vehiculo(self, vehiculo: Vehiculo) -> None:
        """
        Agrega un vehículo al concesionario.

        :param vehiculo: Vehículo a agregar.
        :type vehiculo: Vehiculo
        """
        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self) -> List[str]:
        """
        Devuelve la lista de descripciones de los vehículos.

        :return: Lista de descripciones.
        :rtype: list[str]
        """
        return [v.descripcion() for v in self.vehiculos]
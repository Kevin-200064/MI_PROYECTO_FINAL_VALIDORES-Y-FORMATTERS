"""
Modulo de Utilidades - Validadores
Define funciones para validar entrada de datos
"""
from typing import List
from ..models.producto import Categoria 

class Validadores:
    """Clase con metodos estaticos para validaciones de datos."""

    @staticmethod
    def validar_precio_positivo(precio: float) -> bool:
        """Valida que el precio sea un número positivo."""
        if not isinstance(precio, (int, float)):
            # Permite 0, pero no negativo.
            raise ValueError("El precio debe ser un numero (entero o decimal)")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        return True

    
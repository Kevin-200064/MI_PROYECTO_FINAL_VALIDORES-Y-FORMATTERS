"""
Modulo de Utilidades - Formateadores
Define funciones para formatear y presentar datos
"""

from typing import List, Dict, Any
from ..models.producto import Producto


class Formateadores:
    """Clase con metodos estaticos para formatear datos para la interfaz."""

    @staticmethod
    def formatear_precio(precio: float) -> str:
        """Formatea precio con simbolo de moneda y dos decimales."""
        return f"${precio:,.2f}"

    @staticmethod
    def formatear_producto_tabla(producto: Producto) -> str:
        """Formatea un solo producto para visualizacion en una fila de tabla."""
        precio_formateado = Formateadores.formatear_precio(producto.precio).replace("$", "")
        valor_total_formateado = Formateadores.formatear_precio(producto.calcular_valor_total()).replace("$", "")
        
        return (f"| {producto.id_producto:>6} | {producto.nombre:<20} | "
                f"{precio_formateado:>8} | {producto.cantidad:>6} | "
                f"{valor_total_formateado:>10} |")

    
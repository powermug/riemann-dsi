"""
Distributional Stability Index (DSI) Package

A geometric diagnostic tool for Riemann zeta zero distribution.
"""

from .dsi import compute_dsi, compute_dsi_theoretical, dsi_convergence_table
from .dsi import DSI_UNIFORM, DSI_NORMAL, DSI_RH_LIMIT

__version__ = "1.0.0"
__author__ = "Jeonghoon Lee"

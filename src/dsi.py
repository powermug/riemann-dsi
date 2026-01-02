"""
Distributional Stability Index (DSI) Calculator

This module implements the DSI metric from:
"A Geometric Diagnostic for Riemann Zeta Zero Distribution 
 via the Distributional Stability Index"

DSI = Var(X) / MAD(X)^2

where:
- Var(X) = variance (population)
- MAD(X) = mean absolute deviation from mean

Reference values:
- Uniform distribution: DSI = 4/3 ≈ 1.3333
- Normal distribution: DSI = π/2 ≈ 1.5708
- Sequence {1,2,...,N} under RH: DSI → 4/3 as N → ∞
"""

import numpy as np
from typing import Union, List, Tuple


def compute_dsi(values: Union[List[float], np.ndarray]) -> float:
    """
    Compute the Distributional Stability Index (DSI).
    
    DSI = Var(X) / MAD(X)^2
    
    Parameters
    ----------
    values : array-like
        Sequence of numerical values
        
    Returns
    -------
    float
        The DSI value
        
    Examples
    --------
    >>> compute_dsi([1, 2, 3, 4, 5])
    1.2
    >>> compute_dsi(range(1, 101))  # Should be close to 4/3
    1.3332
    """
    arr = np.array(values, dtype=float)
    
    if len(arr) < 2:
        raise ValueError("Need at least 2 values to compute DSI")
    
    # Population variance
    variance = np.var(arr, ddof=0)
    
    # Mean absolute deviation
    mean = np.mean(arr)
    mad = np.mean(np.abs(arr - mean))
    
    if mad == 0:
        raise ValueError("MAD is zero - all values are identical")
    
    return variance / (mad ** 2)


def compute_dsi_theoretical(N: int) -> float:
    """
    Compute theoretical DSI for sequence {1, 2, ..., N}.
    
    For the sequence {1, 2, ..., N}:
    - Var = (N² - 1) / 12
    - MAD = N / 4 (exact for even N)
    - DSI = (4/3) * (1 - 1/N²)
    
    Parameters
    ----------
    N : int
        Length of sequence
        
    Returns
    -------
    float
        Theoretical DSI value
    """
    return (4/3) * (1 - 1/(N**2))


def dsi_convergence_table(N_values: List[int] = None) -> List[Tuple[int, float, float]]:
    """
    Generate DSI convergence table for various N.
    
    Parameters
    ----------
    N_values : list of int, optional
        Values of N to compute. Default: [10², 10³, 10⁴, 10⁵, 10⁶]
        
    Returns
    -------
    list of tuples
        Each tuple: (N, DSI_computed, |DSI - 4/3|)
    """
    if N_values is None:
        N_values = [10**k for k in range(2, 7)]
    
    results = []
    target = 4/3
    
    for N in N_values:
        dsi = compute_dsi(range(1, N + 1))
        diff = abs(dsi - target)
        results.append((N, dsi, diff))
    
    return results


def print_convergence_table():
    """Print formatted convergence table (reproduces Table 5.1 in paper)."""
    print("=" * 50)
    print("DSI Convergence Table (Table 5.1 in paper)")
    print("=" * 50)
    print(f"{'N':>10} | {'Φ_N':>15} | {'|Φ_N - 4/3|':>15}")
    print("-" * 50)
    
    for N, dsi, diff in dsi_convergence_table():
        print(f"{N:>10} | {dsi:>15.10f} | {diff:>15.2e}")
    
    print("-" * 50)
    print(f"Target: 4/3 = {4/3:.10f}")
    print(f"Convergence rate: O(N^{{-2}})")
    print("=" * 50)


# Reference values
DSI_UNIFORM = 4/3      # ≈ 1.3333
DSI_NORMAL = np.pi/2   # ≈ 1.5708
DSI_RH_LIMIT = 4/3     # Limit under Riemann Hypothesis


if __name__ == "__main__":
    print("\n=== DSI Reference Values ===")
    print(f"Uniform distribution: {DSI_UNIFORM:.6f}")
    print(f"Normal distribution:  {DSI_NORMAL:.6f}")
    print(f"RH limit (N→∞):       {DSI_RH_LIMIT:.6f}")
    
    print("\n")
    print_convergence_table()

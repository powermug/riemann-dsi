"""
Perturbation Sensitivity Analysis for DSI

This module demonstrates how DSI responds to hypothetical
off-critical-line zeros (reproduces Table 5.2 in paper).

The model: Under RH, R_k = k (uniform spacing).
With perturbation: some R_k are shifted, adding variance.
"""

import numpy as np
from typing import List, Tuple
from dsi import compute_dsi


def compute_perturbed_dsi(
    N: int,
    perturbation_fraction: float,
    perturbation_magnitude: float = 0.1
) -> float:
    """
    Compute DSI with perturbed sequence.
    
    Model: R_k = k for most zeros, but a fraction are perturbed by
    adding noise proportional to k.
    
    Parameters
    ----------
    N : int
        Number of zeros
    perturbation_fraction : float
        Fraction of zeros to perturb (0 to 1)
    perturbation_magnitude : float
        Relative magnitude of perturbation
        
    Returns
    -------
    float
        DSI of perturbed sequence
    """
    # Base sequence: R_k = k (RH case)
    R = np.arange(1, N + 1, dtype=float)
    
    # Perturb a fraction of zeros
    n_perturb = int(N * perturbation_fraction)
    if n_perturb > 0:
        # Select random indices to perturb
        np.random.seed(42)  # For reproducibility
        perturb_indices = np.random.choice(N, n_perturb, replace=False)
        
        # Add perturbation: shift by a fraction of k
        # This models zeros being off the critical line
        R[perturb_indices] *= (1 + perturbation_magnitude)
    
    return compute_dsi(R)


def perturbation_sensitivity_table() -> List[Tuple[str, float, float]]:
    """
    Generate perturbation sensitivity table (Table 5.2 in paper).
    
    Returns
    -------
    list of tuples
        Each tuple: (perturbation_description, DSI, deviation_percent)
    """
    target = 4/3
    N = 10000
    
    # Different perturbation scenarios
    scenarios = [
        (0.00, 0.0, "None (RH)"),
        (0.01, 0.5, "1% at σ=0.6"),
        (0.05, 0.5, "5% at σ=0.6"),
        (0.10, 0.5, "10% at σ=0.6"),
    ]
    
    results = []
    for frac, mag, desc in scenarios:
        dsi = compute_perturbed_dsi(N, frac, mag)
        deviation_pct = 100 * (dsi - target) / target
        results.append((desc, dsi, deviation_pct))
    
    return results


def print_sensitivity_table():
    """Print formatted sensitivity table (reproduces Table 5.2 in paper)."""
    print("=" * 60)
    print("DSI Perturbation Sensitivity (Table 5.2 in paper)")
    print("=" * 60)
    print(f"{'Perturbation':>20} | {'Φ_N':>10} | {'Deviation from 4/3':>18}")
    print("-" * 60)
    
    for desc, dsi, dev_pct in perturbation_sensitivity_table():
        print(f"{desc:>20} | {dsi:>10.4f} | {dev_pct:>+17.2f}%")
    
    print("-" * 60)
    print("Note: Off-line zeros increase DSI, moving it away from 4/3")
    print("=" * 60)


if __name__ == "__main__":
    print_sensitivity_table()
    
    print("\n=== Detailed Analysis ===")
    print("\nDSI vs perturbation fraction (magnitude=0.5):")
    for frac in [0.0, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20]:
        dsi = compute_perturbed_dsi(10000, frac, 0.5)
        dev = 100 * (dsi - 4/3) / (4/3)
        print(f"  {frac*100:5.1f}% perturbed: DSI = {dsi:.6f} ({dev:+.2f}%)")

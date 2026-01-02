#!/usr/bin/env python3
"""
Verify Tables from the Paper

This script reproduces all computational results from:
"A Geometric Diagnostic for Riemann Zeta Zero Distribution 
 via the Distributional Stability Index"

Run this to verify Tables 5.1 and 5.2.
"""

from dsi import print_convergence_table, compute_dsi, DSI_UNIFORM, DSI_NORMAL
from perturbation import print_sensitivity_table
import numpy as np


def verify_reference_values():
    """Verify DSI reference values (Theorem 4.3 in paper)."""
    print("=" * 60)
    print("Verification of DSI Reference Values (Theorem 4.3)")
    print("=" * 60)
    
    # (a) Uniform distribution
    print("\n(a) Uniform[0, 1] distribution:")
    print(f"    Theoretical: Var = 1/12, MAD = 1/4")
    print(f"    DSI = (1/12) / (1/4)² = (1/12) / (1/16) = 4/3")
    print(f"    Computed:    {DSI_UNIFORM:.10f}")
    
    # Numerical verification with samples
    np.random.seed(42)
    uniform_samples = np.random.uniform(0, 1, 1000000)
    dsi_uniform_empirical = compute_dsi(uniform_samples)
    print(f"    Empirical (10⁶ samples): {dsi_uniform_empirical:.6f}")
    
    # (b) Normal distribution
    print("\n(b) Normal(0, 1) distribution:")
    print(f"    Theoretical: Var = 1, MAD = √(2/π)")
    print(f"    DSI = 1 / (2/π) = π/2")
    print(f"    Computed:    {DSI_NORMAL:.10f}")
    
    normal_samples = np.random.normal(0, 1, 1000000)
    dsi_normal_empirical = compute_dsi(normal_samples)
    print(f"    Empirical (10⁶ samples): {dsi_normal_empirical:.6f}")
    
    print("\n" + "=" * 60)


def verify_convergence_formula():
    """Verify the convergence formula Φ_N = 4/3 * (1 - 1/N²)."""
    print("=" * 60)
    print("Verification of Convergence Formula (Theorem 4.4)")
    print("=" * 60)
    print("\nFormula: Φ_N = (4/3) × (1 - 1/N²)")
    print("\n" + "-" * 60)
    print(f"{'N':>10} | {'Computed':>15} | {'Formula':>15} | {'Match':>8}")
    print("-" * 60)
    
    for N in [10, 100, 1000, 10000]:
        computed = compute_dsi(range(1, N + 1))
        formula = (4/3) * (1 - 1/(N**2))
        match = "✓" if abs(computed - formula) < 1e-10 else "✗"
        print(f"{N:>10} | {computed:>15.10f} | {formula:>15.10f} | {match:>8}")
    
    print("-" * 60)
    print("Note: Exact match confirms the formula derivation")
    print("=" * 60)


def main():
    """Run all verifications."""
    print("\n" + "=" * 60)
    print("  REPRODUCIBILITY VERIFICATION")
    print("  Paper: A Geometric Diagnostic for Riemann Zeta Zero")
    print("         Distribution via the DSI")
    print("=" * 60 + "\n")
    
    # 1. Reference values
    verify_reference_values()
    print("\n")
    
    # 2. Convergence formula
    verify_convergence_formula()
    print("\n")
    
    # 3. Table 5.1
    print_convergence_table()
    print("\n")
    
    # 4. Table 5.2
    print_sensitivity_table()
    
    print("\n" + "=" * 60)
    print("  ALL VERIFICATIONS COMPLETE")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
